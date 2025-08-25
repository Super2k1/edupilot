from django.db import models
from core.models import AbstractBaseModel

class ClassLevel(AbstractBaseModel):
    """Class/Grade levels"""
    name = models.CharField(max_length=100)  # Grade 1, Grade 2, etc.
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='class_levels'
    )
    description = models.TextField(blank=True)
    monthly_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        unique_together = ['name', 'school']
        ordering = ['name']
    
    def __str__(self):
        return f"{self.school.name} - {self.name}"

class Student(AbstractBaseModel):
    """Student model"""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    # Link to converted lead
    converted_from_lead = models.OneToOneField(
        'lead.Lead', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='converted_student'
    )
    
    # Basic Info
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    # Contact Info
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField()
    
    # Parent/Guardian Info
    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=20)
    parent_email = models.EmailField(blank=True)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=20)
    
    # School Info
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='students'
    )
    enrollment_date = models.DateField()
    
    class Meta:
        ordering = ['student_id']
    
    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"

class Enrollment(AbstractBaseModel):
    """Student enrollment in classes"""
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('graduated', 'Graduated'),
        ('transferred', 'Transferred'),
        ('dropped', 'Dropped Out'),
        ('suspended', 'Suspended'),
    ]
    
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    class_level = models.ForeignKey(
        ClassLevel, 
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.student} enrolled in {self.class_level}"

class Attendance(AbstractBaseModel):
    """Daily attendance records"""
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
    ]
    
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    class_level = models.ForeignKey(
        ClassLevel, 
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)
    marked_by = models.ForeignKey(
        'accounts.StaffProfile', 
        on_delete=models.CASCADE,
        related_name='attendance_marked'
    )
    
    class Meta:
        unique_together = ['student', 'class_level', 'date']
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.student} - {self.date} - {self.get_status_display()}"
