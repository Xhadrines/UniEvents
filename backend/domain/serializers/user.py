from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    # Serializer pentru tabela auth_user generata automat de Django
    password = serializers.CharField(write_only=True, required=False, allow_blank=False)

    class Meta:
        model = User
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
        read_only_fields = ["id", "date_joined", "last_login"]
        extra_kwargs = {
            "is_superuser": {"required": False},
            "is_staff": {"required": False},
            "is_active": {"required": False},
        }

    def create(self, validated_data):
        # Parola trebuie salvata criptat, nu direct in baza de date
        password = validated_data.pop("password")

        if not password:
            raise serializers.ValidationError({"password": "Password is required"})

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # Daca se actualizeaza parola, trebuie criptata din nou
        password = validated_data.pop("password", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance
