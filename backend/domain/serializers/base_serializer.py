from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    # Campuri comune pentru toate serializerele
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
