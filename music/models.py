from django.db import models


class Album(models.Model):

    artist = models.CharField(max_length=250)

    album_title = models.CharField(max_length=350)

    genre = models.CharField(max_length=250)

    album_logo = models.CharField(max_length=350)

    def __str__(self):
        return self.album_title + ' _ ' + self.artist


class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    File_Type = models.CharField(max_length=20)

    song_title = models.CharField(max_length=350)

    is_fav=models.BooleanField(default=False)
    def __str__(self):
        return self.song_title

