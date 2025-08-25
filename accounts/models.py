from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import AbstractBaseModel

class CustomUser(AbstractUser):
    """Custom user model with email as username"""
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        related_name='users'
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email

class StaffProfile(AbstractBaseModel):
    """Staff profile linked to user and school"""
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('teacher', 'Teacher'),
        ('accountant', 'Accountant'),
        ('receptionist', 'Receptionist'),
    ]
    
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='staff_profile'
    )
    school = models.ForeignKey(
        'core.School', 
        on_delete=models.CASCADE,
        related_name='staff_members'
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    hire_date = models.DateField()
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_role_display()}"