from __future__ import unicode_literals

from django.db import models


class PhotoDate(models.Model):
    uploaded_date = models.DateField(unique=True)

    def __str__(self):
        return str(self.uploaded_date) + " hahaha"


class Photo(models.Model):
    photodate = models.ForeignKey(PhotoDate)
    photo = models.ImageField()

    # def __str__(self):
    #     return str(self.photo)