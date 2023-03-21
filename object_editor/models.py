from django.db import models

# Create your models here.


class TextObject(models.Model):
    text = models.CharField(max_length=3)
