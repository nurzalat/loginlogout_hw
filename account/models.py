from django.db import models


class CustomUser(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
