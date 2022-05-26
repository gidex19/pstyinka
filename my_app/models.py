from django.db import models
import mutagen
from mutagen.wave import WAVE
from ckeditor.fields import RichTextField
from .validators import image_validator

# Create your models here.
category_list = (('Glory Tabernacle Summit','Glory Tabernacle Summit'), ('International Youth Summit','International Youth Summit'), ('Mixed Messages', 'Mixed Messages'), ('Spontaneous Sermos', 'Spontaneous Sermos'), ('Ministers Summit','Ministers Summit'))
class Audio(models.Model):
    audio_file = models.FileField(upload_to='media', null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    desctiption  = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, choices=category_list)
    date_uploaded  = models.DateField(auto_now_add=True)

    # def save(self):
    #     super().save()
    #     voice = WAVE(self.audio_file)
    #     print(voice)

# class Post(models.Model):
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=125)
    author = models.CharField(max_length=125)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank = True, null=True, upload_to='post_pics', validators=[image_validator])

    def __str__(self):
        return ('Post: {}, by: {}'.format(self.title, self.author))