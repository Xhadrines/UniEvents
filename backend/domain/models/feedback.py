from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

from .base_model import BaseModel
from .event import Event


class Feedback(BaseModel):
    """
    Model utilizat pentru feedback-ul oferit
    de utilizatori după participarea la evenimente.

    Feedback-ul permite:
    - evaluarea evenimentelor,
    - colectarea opiniilor participanților,
    - analiză de sentiment,
    - îmbunătățirea experienței utilizatorilor.
    """

    # =====================================================
    # RELATIONS
    # =====================================================

    # Utilizatorul care oferă feedback.
    #
    # Dacă utilizatorul este șters,
    # feedback-ul este eliminat automat.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="feedbacks",
    )

    # Evenimentul evaluat.
    #
    # Dacă evenimentul este șters,
    # feedback-urile asociate sunt eliminate.
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="feedbacks",
    )

    # =====================================================
    # FEEDBACK DATA
    # =====================================================

    # Rating numeric între 1 și 5.
    #
    # Validatorii asigură:
    # - minim 1,
    # - maxim 5.
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    # Comentariu opțional.
    #
    # Utilizatorul poate adăuga:
    # - impresii,
    # - sugestii,
    # - observații.
    comment = models.TextField(blank=True)

    # =====================================================
    # SENTIMENT ANALYSIS
    # =====================================================

    # Scor numeric pentru analiza de sentiment.
    #
    # Exemple:
    # - 0.95 -> foarte pozitiv
    # - -0.60 -> negativ
    sentiment_score = models.FloatField(
        null=True,
        blank=True,
    )

    # Eticheta sentimentului.
    #
    # Exemple:
    # - positive
    # - neutral
    # - negative
    sentiment_label = models.CharField(
        max_length=50,
        blank=True,
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a feedback-ului.
        """

        return f"{self.event.name} - " f"{self.rating}/5"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "feedbacks"

        # Un utilizator poate adăuga
        # un singur feedback per eveniment.
        unique_together = (
            "user",
            "event",
        )
