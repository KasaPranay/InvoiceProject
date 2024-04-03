from rest_framework import generics
from .models import InvoiceHeader
from rest_framework.exceptions import ValidationError
from .serializers import InvoiceHeaderSerializer

# Create your views here.


class InvoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = InvoiceHeader.objects.all()
    serialize_classes = InvoiceHeaderSerializer

    def perform_create(self,serializer):
        invoice_data = self.request.data
        invoice_items_data = invoice_data.get('invoice_items',[])

        total_amount = 0

        for item_data in invoice_items_data:
            quantity = item_data.get('quantity',0)
            price = item_data.get('price',0)
            amount = item_data.get('amount',0)

            if quantity <=0 or price <=0 or amount <= 0:
                raise ValidationError('Quantity, price ana amount must be greater than zero')

            invoice_total_amount = invoice_data.get('total_amount',0)

            if total_amount != invoice_total_amount:
                raise ValidationError('Total amount does not match sum of invoice item amounts')

            serializer.save()

    def perform_update(self,serializer):
        invoice_data = self.request.data
        invoice_items_data = invoice_data.get('invoice_items',[])

        total_amount = 0

        for item_data in invoice_items_data:
            quantity = item_data.get('quantity',0)
            price = item_data.get('price',0)
            amount = item_data.get('amount',0)

            if quantity <=0 or price <=0 or amount <= 0:
                raise ValidationError('Quantity, price ana amount must be greater than zero')

            calculated_amount = quantity * price

            if amount != calculated_amount:
                raise ValidationError('Amount must be equal to Quantity*Price')

            total_amount += amount

        invoice_total_amount = invoice_data.get('total_amount',0)

        if total_amount !=invoice_total_amount:
            raise ValidationError('Total amount does not match sum of invoice items amounts')

        serializer.save()

class InvoiceRetrieveUpdateDestroyAPIView(generics.ListCreateAPIView):
    queryset = InvoiceHeader.objects.all()
    serialize_classes = InvoiceHeaderSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_delete(self, instance):
        instance.delete()



