from django.db import models
from apps.core.models import TimeStampModel


class Artist(TimeStampModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artist"

    def __str__(self):
        return self.name
