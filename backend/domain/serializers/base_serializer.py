from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """
    Serializer de bază utilizat de toate
    serializer-ele aplicației.

    Acest serializer oferă câmpuri comune:
    - id,
    - created_at,
    - updated_at.

    Toate serializer-ele aplicației
    moștenesc această clasă.
    """

    # =====================================================
    # COMMON READ-ONLY FIELDS
    # =====================================================

    # ID-ul unic al obiectului.
    #
    # Este generat automat de baza de date
    # și nu poate fi modificat.
    id = serializers.IntegerField(read_only=True)

    # Data și ora creării obiectului.
    #
    # Setată automat la creare.
    created_at = serializers.DateTimeField(read_only=True)

    # Data și ora ultimei actualizări.
    #
    # Actualizată automat la fiecare modificare.
    updated_at = serializers.DateTimeField(read_only=True)
