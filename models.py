from django.db import models


class InvoiceHeader(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    date = models.DateTimeField()
    invoice_number = models.IntegerField(unique=True)
    customer_name = models.CharField(max_length=100)
    billing_address= models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=100)
    GSTIN = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)

class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    invoice = models.ForeignKey(InvoiceHeader,on_delete=models.CASCADE,related_name='invoice_items')
    item_name = models.CharField(max_length=10)
    quantity = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    amount = models.DecimalField(max_digits=10,decimal_places=2)

class InvoiceBillSundry(models.Model):
    id = models.UUIDField(primary_key=True,editable=False)
    invoice = models.ForeignKey(InvoiceHeader,on_delete=models.CASCADE,related_name='invoice_bill_sundrys')
    bill_sundry_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)



