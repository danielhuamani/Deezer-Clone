from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey("albums.Album", related_name="songs", on_delete=models.CASCADE)
    artist = models.ForeignKey("artists.Artist", related_name="songs", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Song"

    def __str__(self):
        return self.name
