from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from info.serializers import SampleLogSerializer
from rest_framework import generics

from info.form import ChainOfCustody, NewCustomer
from info.models import Customer, SampleLog

# Create your views here.
def index (request):
	return render(request,'info/index.html')

class LogBookView(ListView):
	template_name = 'info/logbook.html'
	context_object_name = 'samplelog'

	def get_queryset(self):
		return SampleLog.objects.order_by('-lab_number')

class ChainOfCustodyView(DetailView):
	model = SampleLog
	template_name = 'info/chainofcustody.html'

class CurrentCustomerView(ListView):
	template_name = 'info/customers.html'
	context_object_name = 'customers'

	def get_queryset(self):
		return Customer.objects.order_by('company_name')

class CustomerInfoView(DetailView):
	model = Customer
	template_name = 'info/customerinfo.html'

class SampleLogList(generics.ListCreateAPIView):
	queryset = SampleLog.objects.all()
	serializer_class = SampleLogSerializer

class SampleLogDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = SampleLog.objects.all()
	serializer_class = SampleLogSerializer

class LogCreate(CreateView):
	model = SampleLog
	fields = ['customer', 'product_order', 'date_received', 'lab_number', 'invoice_number', 'rush', 'product_name', 'lot_number', 'item_number', 'test_request', 'notes']

class LogUpdate(UpdateView):
	model = SampleLog
	fields = ['customer', 'product_order', 'date_received', 'lab_number', 'invoice_number', 'rush', 'product_name', 'lot_number', 'item_number', 'test_request', 'notes']
	
class CustomerCreate(CreateView):
	model = Customer
	fields = ['company_name','address', 'city', 'state', 'zipcode', 'telephone', 'fax_number', 'email', 'contact_customer', 'comments']

class CustomerUpdate(UpdateView):
	model = Customer
	fields = ['company_name','address', 'city', 'state', 'zipcode', 'telephone', 'fax_number', 'email', 'contact_customer', 'comments']