from rest_framework import serializers

from ..models import UserProfile

from .base_serializer import BaseSerializer


class UserProfileSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul UserProfile.

    Acest serializer permite:
    - serializarea profilurilor utilizatorilor,
    - validarea relației facultate–specializare,
    - gestionarea datelor academice,
    - integrarea Google OAuth,
    - transformarea obiectelor UserProfile în JSON.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = UserProfile

        # Câmpurile expuse în API.
        fields = [
            "id",
            "user",
            "status",
            "role",
            "faculty",
            "specialization",
            "study_year",
            "group",
            "semi_group",
            "google_sub",
            "is_google_student",
            "created_at",
            "updated_at",
        ]

        # Câmpuri read-only:
        # nu pot fi modificate direct prin request.
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

        # Configurări opționale pentru validare
        # și comportament în API.
        extra_kwargs = {
            "faculty": {
                "required": False,
                "allow_null": True,
            },
            "specialization": {
                "required": False,
                "allow_null": True,
            },
            "study_year": {
                "required": False,
                "allow_null": True,
            },
            "group": {
                "required": False,
                "allow_null": True,
            },
            "semi_group": {
                "required": False,
                "allow_null": True,
            },
            "google_sub": {
                "required": False,
                "allow_null": True,
            },
            "is_google_student": {
                "required": False,
            },
        }

    # =====================================================
    # VALIDATION
    # =====================================================

    def validate(self, attrs):
        """
        Validează consistența dintre:
        - facultate
        - specializare

        Reguli:
        - dacă există specializare, aceasta trebuie
          să aparțină facultății selectate
        - dacă facultatea nu este trimisă,
          este dedusă din specializare
        """

        specialization = attrs.get("specialization")
        faculty = attrs.get("faculty")

        if specialization:

            # Verificăm consistența facultății
            if faculty and specialization.faculty_id != faculty.id:
                raise serializers.ValidationError(
                    {
                        "specialization": (
                            "Specializarea nu apartine " "facultatii selectate."
                        )
                    }
                )

            # Dacă nu a fost trimisă facultatea,
            # o deducem automat din specializare.
            attrs["faculty"] = specialization.faculty

        return attrs
