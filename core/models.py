from django.db import models

# Create your models here.
class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class School(AbstractBaseModel):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='school_logos/', blank=True, null=True)
    
    # Settings
    currency = models.CharField(max_length=10, default='MAD')
    timezone = models.CharField(max_length=50, default='Africa/Casablanca')
    academic_year_start = models.DateField()
    
    def __str__(self):
        return self.name