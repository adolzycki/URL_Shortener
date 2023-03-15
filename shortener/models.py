from django.db import models


class ShortendURL(models.Model):
    short_url = models.CharField(max_length=8, unique=True)
    full_url = models.URLField(max_length=200)
