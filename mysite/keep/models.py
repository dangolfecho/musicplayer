from django.db import models
from datetime import datetime

# Create your models here.

class Note(models.Model):
    text = models.CharField(max_length=200)
    last_modified = models.CharField(max_length=200,default=datetime.now().strftime("%Y-%m-%d %H:%M"))