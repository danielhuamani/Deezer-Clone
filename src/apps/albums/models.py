from django.db import models
from apps.core.models import TimeStampModel


class Album(TimeStampModel):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey("artists.Artist", related_name="albums", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Album"

    def __str__(self):
        return self.title
