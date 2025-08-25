from django.db import models
from core.models import AbstractBaseModel

class Invoice(AbstractBaseModel):
    """Student invoices"""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    ]
    
    invoice_number = models.CharField(max_length=20, unique=True)
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE,
        related_name='invoices'
    )
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='invoices'
    )
    
    # Amount Details
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    late_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Dates
    issue_date = models.DateField()
    due_date = models.DateField()
    
    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    
    # Who created/modified
    created_by = models.ForeignKey(
        'accounts.StaffProfile', 
        on_delete=models.CASCADE,
        related_name='invoices_created'
    )
    
    class Meta:
        ordering = ['-issue_date']
    
    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.student}"

class InvoiceItem(AbstractBaseModel):
    """Individual items on an invoice"""
    invoice = models.ForeignKey(
        Invoice, 
        on_delete=models.CASCADE, 
        related_name='items'
    )
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.description} - {self.total_price}"

class Payment(AbstractBaseModel):
    """Payment records"""
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('card', 'Credit/Debit Card'),
        ('check', 'Check'),
        ('online', 'Online Payment'),
    ]
    
    payment_reference = models.CharField(max_length=20, unique=True)
    invoice = models.ForeignKey(
        Invoice, 
        on_delete=models.CASCADE, 
        related_name='payments'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateField()
    transaction_reference = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    
    received_by = models.ForeignKey(
        'accounts.StaffProfile', 
        on_delete=models.CASCADE,
        related_name='payments_received'
    )
    
    class Meta:
        ordering = ['-payment_date']
    
    def __str__(self):
        return f"Payment {self.payment_reference} - {self.amount}"