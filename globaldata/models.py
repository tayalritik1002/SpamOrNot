from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    phone_number = models.CharField(max_length=15,primary_key=True)
    name = models.CharField(max_length=50)
    spam_count = models.IntegerField(default=0)

