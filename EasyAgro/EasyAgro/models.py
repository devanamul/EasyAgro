from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class crops(models.Model):
	name = models.CharField(max_length=150)

class project(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	crop = models.ForeignKey(crops, on_delete=models.CASCADE)
	area = models.FloatField()
	currentN = models.FloatField()
	currentP = models.FloatField()
	currentK =  models.FloatField()
	status = models.CharField(max_length=25)

class fertilizer(models.Model):
	crop = models.ForeignKey(crops, on_delete=models.CASCADE)
	nitrogen = models.FloatField()
	phosphorous = models.FloatField()
	potassium =  models.FloatField()

class postPlantingProcess(models.Model):
	crop = models.ForeignKey(crops, on_delete=models.CASCADE)
	fieldPreparation = models.CharField(max_length=300)
	depth = models.FloatField()
	spacing = models.CharField(max_length=200)
	drainage = models.CharField(max_length=200)