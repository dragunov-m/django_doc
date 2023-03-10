from django.db import models


class Text(models.Model):
    text = models.CharField(max_length=3, primary_key=True)
