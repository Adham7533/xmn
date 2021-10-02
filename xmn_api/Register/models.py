from django.db import models


# Create your models here.
class User(models.Model):
    firs_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=255, blank=False)
    email = models.EmailField('Email', max_length=100, blank=False)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username
