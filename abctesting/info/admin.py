from django.contrib import admin

# Register your models here.
from .models import Customer, SampleLog 

class CustomerAdmin(admin.ModelAdmin):
	
	fieldsets = [
        (None,               {'fields': ['company_name']}),
        ('Customer information', {'fields': ['address','city','state','zipcode','telephone','fax_number','email','contact_customer','comments']}),
    ]

	list_display = ('company_name','contact_customer')

	search_fields = ['company_name','contact_customer']

class SampleLogAdmin(admin.ModelAdmin):
	
	fieldsets = [
        (None,               {'fields': ['customer']}),
        ('Chain of custody', {'fields': ['product_order','date_received','lab_number','invoice_number','product_name','lot_number','item_number','test_request','notes']}),
    ]
	list_display = ('lab_number','customer')

	search_fields = ['lab_number','customer__company_name','date_received']
 		 
admin.site.register(Customer, CustomerAdmin)
admin.site.register(SampleLog, SampleLogAdmin)