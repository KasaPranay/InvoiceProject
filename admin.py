from django.contrib import admin

from .models import InvoiceHeader,InvoiceItem,InvoiceBillSundry
# Register your models here.

admin.site.register('type')
admin.site.register(InvoiceHeader)
admin.site.register(InvoiceItem)
admin.site.register(InvoiceBillSundry)


