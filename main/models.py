from django.db import models

# Create your models here.
class shorted_urls(models.Model):
    short_url=models.CharField(max_length=25)
    long_url=models.URLField("URL",unique=True)