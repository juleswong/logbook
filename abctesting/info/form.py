from django import forms

from info.models import SampleLog, Customer

class ChainOfCustody(forms.ModelForm):

	class Meta:
		model = SampleLog
		fields = ('customer', 'product_order', 'date_received', 'lab_number', 'invoice_number', 'rush', 'product_name', 'lot_number', 'item_number', 'test_request', 'notes')
		
class NewCustomer(forms.ModelForm):
	
	class Meta:
		model = Customer
		fields =('company_name','address', 'city', 'state', 'zipcode', 'telephone', 'fax_number', 'email', 'contact_customer', 'comments')