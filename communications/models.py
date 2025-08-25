from django.db import models
from core.models import AbstractBaseModel

class MessageTemplate(AbstractBaseModel):
    """Reusable message templates"""
    TYPE_CHOICES = [
        ('welcome', 'Welcome Message'),
        ('payment_reminder', 'Payment Reminder'),
        ('fee_due', 'Fee Due Notice'),
        ('absence_alert', 'Absence Alert'),
        ('general', 'General Communication'),
        ('event_reminder', 'Event Reminder'),
    ]
    
    name = models.CharField(max_length=100)
    template_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='message_templates'
    )
    subject = models.CharField(max_length=200, blank=True)  # For email
    message_body = models.TextField()
    
    # Template variables like {{student_name}}, {{amount}}
    available_variables = models.JSONField(default=list)
    
    class Meta:
        unique_together = ['name', 'school']
    
    def __str__(self):
        return f"{self.name} - {self.get_template_type_display()}"

class MessageLog(AbstractBaseModel):
    """Log of all sent messages"""
    CHANNEL_CHOICES = [
        ('whatsapp', 'WhatsApp'),
        ('sms', 'SMS'),
        ('email', 'Email'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('delivered', 'Delivered'),
        ('read', 'Read'),
        ('failed', 'Failed'),
    ]
    
    # Recipient Info
    recipient_name = models.CharField(max_length=100)
    recipient_phone = models.CharField(max_length=20, blank=True)
    recipient_email = models.EmailField(blank=True)
    
    # Message Details
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    template_used = models.ForeignKey(
        MessageTemplate, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    subject = models.CharField(max_length=200, blank=True)
    message_body = models.TextField()
    
    # Tracking
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='message_logs'
    )
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='messages_received'
    )
    sent_by = models.ForeignKey(
        'accounts.StaffProfile', 
        on_delete=models.CASCADE,
        related_name='messages_sent'
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    # External service tracking
    external_message_id = models.CharField(max_length=100, blank=True)
    
    # Timestamps
    sent_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    read_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_channel_display()} to {self.recipient_name}"

class Event(AbstractBaseModel):
    """Calendar events and reminders"""
    EVENT_TYPE_CHOICES = [
        ('reminder', 'Reminder'),
        ('meeting', 'Meeting'),
        ('payment_due', 'Payment Due'),
        ('school_event', 'School Event'),
        ('holiday', 'Holiday'),
        ('exam', 'Exam'),
        ('parent_meeting', 'Parent Meeting'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)
    
    # Timing
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)
    all_day = models.BooleanField(default=False)
    
    # Associations
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='events'
    )
    student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='events'
    )
    staff_members = models.ManyToManyField(
        'accounts.StaffProfile', 
        blank=True,
        related_name='events_assigned'
    )
    
    # Notifications
    send_reminder = models.BooleanField(default=False)
    reminder_minutes_before = models.PositiveIntegerField(default=60)
    reminder_sent = models.BooleanField(default=False)
    
    created_by = models.ForeignKey(
        'accounts.StaffProfile', 
        on_delete=models.CASCADE,
        related_name='events_created'
    )
    
    class Meta:
        ordering = ['start_datetime']
    
    def __str__(self):
        return f"{self.title} - {self.start_datetime.strftime('%Y-%m-%d %H:%M')}"

class Notification(AbstractBaseModel):
    """In-app notifications"""
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    title = models.CharField(max_length=200)
    message = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    
    # Recipients
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    recipient = models.ForeignKey(
        'accounts.StaffProfile', 
        on_delete=models.CASCADE,
        related_name='notifications_received'
    )
    
    # Status
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    
    # Related Objects (optional)
    related_student = models.ForeignKey(
        'students.Student', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    related_invoice = models.ForeignKey(
        'payments.Invoice', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    related_event = models.ForeignKey(
        Event, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.recipient.user.get_full_name()}"