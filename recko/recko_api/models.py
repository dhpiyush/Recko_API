from django.db import models

# Create your models here.

class universe(models.Model):
	universe_name = models.CharField(max_length=50,unique=True,default="")


class family(models.Model):
	family_name = models.CharField(max_length=50,unique=True,default="")

class person(models.Model):
	person_name = models.CharField(max_length=50,unique=True,default="")
	family = models.ForeignKey(family, related_name="fname",blank=True, null=True)
	universe = models.ForeignKey(universe,related_name="uname",blank=True, null=True)
	power = models.IntegerField(blank=True, null=True)