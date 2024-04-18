# converter/models.py

from django.db import models

class TextInput(models.Model):
    text = models.TextField()
    html_output = models.TextField(blank=True, null=True)
