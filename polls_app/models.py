from django.db import models


class Polls(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=200, null=True)
    option2 = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="my_image/")


class Profile(models.Model):
    username = models.TextField()
    password = models.TextField()


    def __unicode__(self):
        return "Username: %s and password is: %s" % (self.username, self.password)