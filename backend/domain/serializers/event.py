from rest_framework import serializers

from ..models import (
    Event,
    Organizer,
    Location,
    Category,
    ParticipationType,
    Status,
)

from .base_serializer import BaseSerializer
from .organizer import OrganizerSerializer
from .location import LocationSerializer
from .category import CategorySerializer
from .participation_type import (
    ParticipationTypeSerializer,
)
from .status import StatusSerializer
from .faculty import FacultySerializer


class EventSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Event.

    Acest serializer gestionează:
    - serializarea evenimentelor,
    - validarea datelor,
    - relațiile nested,
    - afișarea câmpurilor calculate,
    - normalizarea politicilor de acces,
    - logica de creare și actualizare.
    """

    # =====================================================
    # NESTED SERIALIZERS
    # =====================================================

    # Organizatorul evenimentului.
    organizer = OrganizerSerializer(read_only=True)

    # Locația evenimentului.
    location = LocationSerializer(read_only=True)

    # Categoria evenimentului.
    category = CategorySerializer(read_only=True)

    # Tipul de participare.
    participation_type = ParticipationTypeSerializer(read_only=True)

    # Statusul evenimentului.
    status = StatusSerializer(read_only=True)

    # =====================================================
    # WRITE-ONLY RELATION FIELDS
    # =====================================================

    # ID organizator.
    #
    # Utilizat la creare/update.
    organizer_id = serializers.PrimaryKeyRelatedField(
        queryset=Organizer.objects.all(),
        source="organizer",
        write_only=True,
        required=False,
    )

    # ID locație.
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(),
        source="location",
        write_only=True,
    )

    # ID categorie.
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True,
    )

    # ID tip participare.
    participation_type_id = serializers.PrimaryKeyRelatedField(
        queryset=ParticipationType.objects.all(),
        source="participation_type",
        write_only=True,
    )

    # ID status.
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
        source="status",
        write_only=True,
        required=False,
    )

    # =====================================================
    # COMPUTED / EXTRA FIELDS
    # =====================================================

    # Facultatea asociată organizatorului.
    faculty = FacultySerializer(
        read_only=True,
        source="organizer.faculty",
    )

    # Numărul de înscrieri.
    registered_count = serializers.SerializerMethodField()

    # Statusul înscrierii utilizatorului curent.
    user_registration_status = serializers.SerializerMethodField()

    # Varianta display pentru pricing_type.
    pricing_type_display = serializers.SerializerMethodField()

    # Varianta display pentru access_policy.
    access_policy_display = serializers.SerializerMethodField()

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Model asociat serializer-ului.
        model = Event

        # Câmpurile expuse în API.
        fields = [
            "id",
            "name",
            "description",
            "registration_link",
            "online_link",
            "organizer",
            "faculty",
            "location",
            "category",
            "participation_type",
            "status",
            "organizer_id",
            "location_id",
            "category_id",
            "participation_type_id",
            "status_id",
            "start_date",
            "end_date",
            "capacity",
            "registered_count",
            "user_registration_status",
            "registration_deadline",
            "pricing_type",
            "access_policy",
            "is_free_entry",
            "requires_registration",
            "requires_ticket",
            "qr_code",
            "max_files",
            "max_file_size_mb",
            "validated_by",
            "validated_at",
            "created_at",
            "updated_at",
            "pricing_type_display",
            "access_policy_display",
        ]

        # Câmpuri read-only.
        read_only_fields = [
            "id",
            "validated_by",
            "validated_at",
            "created_at",
            "updated_at",
        ]

    # =====================================================
    # ACCESS POLICY NORMALIZATION
    # =====================================================

    def _normalize_access_fields(self, attrs):
        """
        Normalizează câmpurile:
        - pricing_type
        - access_policy
        - requires_registration
        - requires_ticket
        - is_free_entry
        """

        data = dict(attrs)

        instance = getattr(
            self,
            "instance",
            None,
        )

        current_is_free = (
            data.get("is_free_entry")
            if "is_free_entry" in data
            else getattr(
                instance,
                "is_free_entry",
                True,
            )
        )

        current_requires_registration = (
            data.get("requires_registration")
            if "requires_registration" in data
            else getattr(
                instance,
                "requires_registration",
                False,
            )
        )

        current_requires_ticket = (
            data.get("requires_ticket")
            if "requires_ticket" in data
            else getattr(
                instance,
                "requires_ticket",
                False,
            )
        )

        # =================================================
        # PRICING TYPE
        # =================================================

        pricing_type = data.get("pricing_type")

        if pricing_type is None:
            pricing_type = "free" if current_is_free else "paid"

        # =================================================
        # ACCESS POLICY
        # =================================================

        access_policy = data.get("access_policy")

        if access_policy is None:

            if current_requires_registration and current_requires_ticket:
                access_policy = "registration_ticket"

            elif current_requires_registration:
                access_policy = "registration"

            elif current_requires_ticket:
                access_policy = "ticket"

            else:
                access_policy = "open"

        # =================================================
        # NORMALIZED VALUES
        # =================================================

        data["pricing_type"] = pricing_type

        data["access_policy"] = access_policy

        data["is_free_entry"] = pricing_type == "free"

        data["requires_registration"] = access_policy in (
            "registration",
            "registration_ticket",
        )

        data["requires_ticket"] = access_policy in (
            "ticket",
            "registration_ticket",
        )

        return data

    # =====================================================
    # VALIDATION
    # =====================================================

    def validate(self, attrs):
        """
        Rulează normalizarea câmpurilor
        înainte de validare finală.
        """

        return self._normalize_access_fields(attrs)

    # =====================================================
    # CREATE EVENT
    # =====================================================

    def create(self, validated_data):
        """
        Creează un eveniment nou.

        Automat:
        - asociază organizatorul autentificat,
        - setează statusul implicit:
          „In asteptare”.
        """

        request = self.context.get("request")

        organizer = Organizer.objects.filter(user=request.user).first()

        if not organizer:
            raise serializers.ValidationError(
                {
                    "organizer": (
                        "Utilizatorul autentificat " "nu are organizator asociat."
                    )
                }
            )

        # =================================================
        # WAITING STATUS
        # =================================================

        waiting_status = (
            Status.objects.filter(name__iexact="In asteptare").first()
            or Status.objects.filter(name__iexact="În așteptare").first()
            or Status.objects.filter(name__iexact="Lista de asteptare").first()
        )

        if not waiting_status:
            raise serializers.ValidationError(
                {"status": ("Nu există status pentru " "evenimente în așteptare.")}
            )

        validated_data["organizer"] = organizer

        validated_data["status"] = waiting_status

        return super().create(validated_data)

    # =====================================================
    # UPDATE EVENT
    # =====================================================

    def update(
        self,
        instance,
        validated_data,
    ):
        """
        Actualizează evenimentul.

        Restricții:
        - doar administratorii pot modifica
          statusul evenimentului.
        """

        request = self.context.get("request")

        user = request.user if request else None

        role_name = ""

        try:
            role_name = user.userprofile.role.name.lower()

        except Exception:
            role_name = ""

        # =================================================
        # ADMIN CHECK
        # =================================================

        is_admin = bool(
            user
            and (
                user.is_staff
                or user.is_superuser
                or role_name
                in [
                    "admin",
                    "administrator",
                ]
            )
        )

        # Organizatorul nu poate fi schimbat.
        validated_data.pop(
            "organizer",
            None,
        )

        # Doar adminii pot modifica statusul.
        if not is_admin:
            validated_data.pop(
                "status",
                None,
            )

        return super().update(
            instance,
            validated_data,
        )

    # =====================================================
    # DISPLAY HELPERS
    # =====================================================

    def get_pricing_type_display(
        self,
        obj: Event,
    ) -> str:
        """
        Returnează varianta display
        pentru pricing_type.
        """

        return obj.get_pricing_type_display()

    def get_access_policy_display(
        self,
        obj: Event,
    ) -> str:
        """
        Returnează varianta display
        pentru access_policy.
        """

        return obj.get_access_policy_display()

    # =====================================================
    # COMPUTED FIELDS
    # =====================================================

    def get_registered_count(
        self,
        obj: Event,
    ) -> int:
        """
        Returnează numărul total
        de înscrieri la eveniment.
        """

        try:
            return obj.registrations.count()

        except AttributeError:
            return 0

    def get_user_registration_status(
        self,
        obj: Event,
    ):
        """
        Returnează statusul înscrierii
        utilizatorului autentificat.
        """

        request = self.context.get("request")

        if not request or not request.user.is_authenticated:
            return None

        registration = (
            obj.registrations.filter(user=request.user).select_related("status").first()
        )

        if not registration or not registration.status:
            return None

        return registration.status.name
