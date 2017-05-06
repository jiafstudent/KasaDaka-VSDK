from django.db import models

class VoiceMessage(models.Model):
    subCategory = models.CharField(max_length=100)
    mainCategory = models.CharField(max_length=100)
    recording = models.FileField()
    # properties