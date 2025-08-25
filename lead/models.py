from django.db import models
from core.models import AbstractBaseModel

class LeadSource(AbstractBaseModel):
    """Sources of leads (Facebook, Walk-in, etc.)"""
    name = models.CharField(max_length=100)
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='lead_sources'
    )
    
    class Meta:
        unique_together = ['name', 'school']
    
    def __str__(self):
        return f"{self.name} - {self.school.name}"

class Lead(AbstractBaseModel):
    """Lead/Prospect model"""
    STATUS_CHOICES = [
        ('inquiry', 'Inquiry'),
        ('contacted', 'Contacted'),
        ('visited', 'Visited School'),
        ('registered', 'Registered'),
        ('dropped', 'Dropped'),
    ]
    
    # Basic Info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    
    # Parent/Guardian Info
    parent_name = models.CharField(max_length=100, blank=True)
    parent_phone = models.CharField(max_length=20, blank=True)
    parent_email = models.EmailField(blank=True)
    
    # CRM Fields
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='leads'
    )
    source = models.ForeignKey(
        LeadSource, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inquiry')
    interested_program = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    
    # Tracking
    assigned_to = models.ForeignKey(
        'accounts.StaffProfile', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='assigned_leads'
    )
    last_contact_date = models.DateField(null=True, blank=True)
    next_follow_up_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_status_display()}"

class FollowUp(AbstractBaseModel):
    """Follow-up activities for leads"""
    TYPE_CHOICES = [
        ('call', 'Phone Call'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
        ('visit', 'In-Person Visit'),
        ('other', 'Other'),
    ]
    
    lead = models.ForeignKey(
        Lead, 
        on_delete=models.CASCADE, 
        related_name='follow_ups'
    )
    staff = models.ForeignKey(
        'accounts.StaffProfile', 
        on_delete=models.CASCADE,
        related_name='follow_ups_created'
    )
    follow_up_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    notes = models.TextField()
    scheduled_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-scheduled_date']
    
    def __str__(self):
        return f"{self.lead} - {self.get_follow_up_type_display()}"
