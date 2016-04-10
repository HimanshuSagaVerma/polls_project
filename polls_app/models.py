from django.db import models


class Polls(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=200, null=True)
    option2 = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="my_image/")
