from django.db import models
from uuid import uuid4

class GameBoard(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4(),
        unique=True,
        blank=False,
        verbose_name="ID"
    )
    # board = 