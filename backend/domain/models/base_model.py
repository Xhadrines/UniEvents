from django.db import models


class BaseModel(models.Model):
    """
    Model de bază abstract utilizat de toate
    entitățile aplicației.

    Acest model oferă:
    - data creării,
    - data ultimei actualizări,
    - funcționalități comune reutilizabile.

    Toate modelele aplicației moștenesc această clasă.
    """

    # =====================================================
    # TIMESTAMPS
    # =====================================================

    # Data și ora creării obiectului.
    #
    # Se setează automat o singură dată,
    # la crearea înregistrării.
    created_at = models.DateTimeField(auto_now_add=True)

    # Data și ora ultimei actualizări.
    #
    # Se actualizează automat la fiecare save().
    updated_at = models.DateTimeField(auto_now=True)

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Model abstract:
        # nu va crea tabel separat în baza de date.
        #
        # Este utilizat doar pentru moștenire.
        abstract = True
