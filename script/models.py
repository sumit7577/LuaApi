from django.db import models

# Create your models here.
class Customer(models.Model):
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=12)
	password = models.CharField(max_length=12)
	device = models.CharField(max_length=20)
	timestamp = models.DateField()
	
	def __str__(self):
		return self.name