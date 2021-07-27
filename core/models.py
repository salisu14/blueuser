from django.db import models
from django.conf import settings
import uuid


class Branch(models.Model):
	id = models.UUIDField(
	  primary_key=True, 
	  default=uuid.uuid4,
	  editable=False	
	)
	name = models.CharField(max_length=200)
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		on_delete=models.CASCADE
	)


	class Meta:
		verbose_name_plural = 'branches'
	
	def __str__(self) -> str:
	    return self.name

class Department(models.Model):
	id = models.UUIDField(
	  primary_key=True, 
	  default=uuid.uuid4,
	  editable=False	
	)
	name = models.CharField(max_length=200)
	branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		on_delete=models.CASCADE
	)



	def __str__(self) -> str:
	    return self.name


class Product(models.Model):
	id = models.UUIDField(
	  primary_key=True, 
	  default=uuid.uuid4,
	  editable=False	
	)
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	created_by = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		on_delete=models.CASCADE
	)


	def __str__(self) -> str:
	    return self.name
