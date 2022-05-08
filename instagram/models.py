from django.db import models

class InstagramAccounts(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class createstory(models.Model):
    type = models.SmallIntegerField()
    template = models.ImageField()
    text1 = models.TextField()
    photoup = models.ImageField()
    photobut = models.ImageField()

class createpost(models.Model):
    type = models.SmallIntegerField()
    template = models.ImageField()
    text1 = models.TextField()
    photoup = models.ImageField()
    photobut = models.ImageField()
    caption = models.TextField(null=True)

class ForIntractUsers(models.Model):
    username = models.CharField(max_length=100)

class Comments(models.Model):
    text = models.CharField(max_length=100)