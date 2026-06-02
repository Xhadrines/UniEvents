from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer utilizat pentru modelul User (auth_user).

    Acest serializer permite:
    - serializarea utilizatorilor Django,
    - crearea și actualizarea utilizatorilor,
    - gestionarea securizată a parolelor,
    - integrarea cu sistemul de autentificare Django.
    """

    # =====================================================
    # PASSWORD FIELD
    # =====================================================

    # Parola este write-only pentru securitate.
    #
    # Nu este returnată niciodată în API response.
    password = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=False,
    )

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = User

        # Câmpurile expuse în API.
        fields = [
            "id",
            "username",
            "email",
            "password",
            "last_name",
            "first_name",
            "is_superuser",
            "is_staff",
            "is_active",
            "last_login",
            "date_joined",
        ]

        # Câmpuri read-only:
        # gestionate automat de Django.
        read_only_fields = [
            "id",
            "date_joined",
            "last_login",
        ]

        # Configurări suplimentare pentru
        # câmpurile de permisiuni.
        extra_kwargs = {
            "is_superuser": {
                "required": False,
            },
            "is_staff": {
                "required": False,
            },
            "is_active": {
                "required": False,
            },
        }

    # =====================================================
    # CREATE USER
    # =====================================================

    def create(self, validated_data):
        """
        Creează un utilizator nou.

        Parola este hash-uită înainte de salvare
        folosind set_password().
        """

        password = validated_data.pop("password")

        if not password:
            raise serializers.ValidationError({"password": ("Password is required")})

        user = User(**validated_data)

        # Hash securizat al parolei
        user.set_password(password)

        user.save()

        return user

    # =====================================================
    # UPDATE USER
    # =====================================================

    def update(self, instance, validated_data):
        """
        Actualizează un utilizator existent.

        Dacă parola este furnizată,
        aceasta este re-hash-uită.
        """

        password = validated_data.pop(
            "password",
            None,
        )

        # Actualizare câmpuri simple
        for key, value in validated_data.items():
            setattr(instance, key, value)

        # Actualizare parolă (dacă există)
        if password:
            instance.set_password(password)

        instance.save()

        return instance
