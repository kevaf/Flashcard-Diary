from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class Cards(models.Model):
    title = models.CharField(max_length=50)
    notes = models.TextField()
    courses = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
