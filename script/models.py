from django.db import models

# Create your models here.
class Customer(models.Model):
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=12)
	password = models.CharField(max_length=12)
	deviceIMEI = models.CharField(max_length=20)
	expiryDate= models.DateField()
	scriptName = models.CharField(max_length=50,default="")
	
	def __str__(self):
		return self.name

class LuaScript(models.Model):
	app_id = models.AutoField
	app = models.FileField(upload_to="templates/shop",default="")