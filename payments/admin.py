from django.contrib import admin

# Register your models here.
from .models import Invoice, Payment, InvoiceItem
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(InvoiceItem)
