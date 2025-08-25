from django.db import models
from core.models import AbstractBaseModel

class LeadScore(AbstractBaseModel):
    """AI-calculated lead scoring"""
    TEMPERATURE_CHOICES = [
        ('hot', 'Hot Lead'),
        ('warm', 'Warm Lead'),
        ('cold', 'Cold Lead'),
    ]
    
    lead = models.OneToOneField(
        'lead.Lead', 
        on_delete=models.CASCADE,
        related_name='ai_score'
    )
    score = models.IntegerField(default=0)  # 0-100
    temperature = models.CharField(max_length=10, choices=TEMPERATURE_CHOICES)
    
    # Scoring Factors
    last_contact_days_ago = models.IntegerField(default=0)
    follow_up_count = models.IntegerField(default=0)
    responded_to_messages = models.BooleanField(default=False)
    visited_school = models.BooleanField(default=False)
    inquiry_to_contact_days = models.IntegerField(default=0)
    
    # Metadata
    calculated_at = models.DateTimeField(auto_now=True)
    algorithm_version = models.CharField(max_length=10, default='1.0')
    
    def __str__(self):
        return f"{self.lead} - {self.score}/100 ({self.get_temperature_display()})"

class AssistantSuggestion(AbstractBaseModel):
    """AI-generated suggestions for staff"""
    SUGGESTION_TYPE_CHOICES = [
        ('follow_up_lead', 'Follow Up with Lead'),
        ('payment_reminder', 'Send Payment Reminder'),
        ('at_risk_student', 'At-Risk Student Alert'),
        ('re_engage_parent', 'Re-engage Parent'),
        ('schedule_meeting', 'Schedule Meeting'),
    ]
    
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    
    suggestion_type = models.CharField(max_length=20, choices=SUGGESTION_TYPE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    
    # AI reasoning
    reasoning = models.TextField(blank=True)
    confidence_score = models.FloatField(default=0.0)  # 0.0 to 1.0
    
    # Associations
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='ai_suggestions'
    )
    assigned_to = models.ForeignKey(
        'accounts.StaffProfile', 
        on_delete=models.CASCADE,
        related_name='ai_suggestions_received'
    )
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    lead = models.ForeignKey(
        'lead.Lead', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    
    # Status
    is_dismissed = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    feedback_rating = models.PositiveIntegerField(null=True, blank=True)  # 1-5 stars
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_suggestion_type_display()} - {self.title}"

class SmartMessage(AbstractBaseModel):
    """AI-generated message suggestions"""
    RECIPIENT_TYPE_CHOICES = [
        ('lead', 'Lead'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    ]
    
    recipient_type = models.CharField(max_length=20, choices=RECIPIENT_TYPE_CHOICES)
    suggested_message = models.TextField()
    
    # AI Context
    context_data = models.JSONField(default=dict)  # What data was used to generate
    generated_by = models.CharField(max_length=50, default='rule_based')  # 'openai', 'rule_based'
    confidence_score = models.FloatField(default=0.0)
    
    # Associations
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='smart_messages'
    )
    lead = models.ForeignKey(
        'lead.Lead', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    
    # Usage Tracking
    was_used = models.BooleanField(default=False)
    was_modified = models.BooleanField(default=False)
    final_message = models.TextField(blank=True)
    user_rating = models.PositiveIntegerField(null=True, blank=True)  # 1-5 stars
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Smart message for {self.recipient_type} - {'Used' if self.was_used else 'Generated'}"