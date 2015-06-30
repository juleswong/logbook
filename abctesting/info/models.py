import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
	company_name = models.CharField(max_length=2000)
	address = models.CharField(max_length=1000,blank=True)
	city = models.CharField(max_length=1000,blank=True)
	state = models.CharField(max_length=20,blank=True)
	zipcode = models.CharField(max_length=200,blank=True)
	telephone = models.CharField(max_length=1000,blank=True)
	fax_number = models.CharField(max_length=500,blank=True)
	email = models.CharField(max_length=500,blank=True)
	contact_customer = models.CharField(max_length=2000,blank=True)
	comments = models.TextField(blank=True)

	def __str__(self):
		return self.company_name

	def get_absolute_url(self):
		return reverse('customerinfo', kwargs={'pk': self.pk})

class SampleLog(models.Model):
	customer = models.ForeignKey(Customer)
	product_order = models.CharField(max_length=500,blank=True)
	date_received = models.DateField()
	rush = models.CharField(max_length=255,blank=True)
	lab_number = models.IntegerField(unique=True)
	invoice_number = models.IntegerField()
	product_name = models.CharField(max_length=2000)
	lot_number = models.CharField(max_length=2000,blank=True)
	item_number = models.CharField(max_length=2000,blank=True)
	test_request = models.TextField()
	notes = models.TextField(blank=True)

	def __str__(self):
		return str(self.lab_number)

	def get_absolute_url(self):
		return reverse('chainofcustody', kwargs={'pk': self.pk})