from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class crops(models.Model):
	name = models.CharField(max_length=150)