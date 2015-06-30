from django.forms import widgets
from rest_framework import serializers
from info.models import SampleLog, Customer

class SampleLogSerializer(serializers.ModelSerializer):
	customer = serializers.StringRelatedField()
	
	class Meta:
		model = SampleLog
		fields =('pk', 'customer', 'product_order', 'date_received', 'lab_number', 'invoice_number', 'rush', 'product_name', 'lot_number', 'item_number', 'test_request', 'notes' )