from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=200, unique=True)

    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
