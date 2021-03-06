from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 2000)
    singer = models.CharField(max_length = 2000)
    genre = models.CharField(max_length= 100)
    image = models.CharField(max_length=100000000, default="")
    song = models.FileField(upload_to = 'images')
    movie = models.CharField(max_length=2000,default= "")
    credit = models.CharField(max_length=100000,default="")
    def __str__(self) :
        return self.name

class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=100000000, default="")
    
class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=100000000, default="")

class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    music = models.CharField(max_length=1000000)

class Favourites(models.Model):
    fav_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_song_id = models.CharField(max_length=100000000, default="")