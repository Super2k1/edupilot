from django.db import models

# Create your models here.
class accounts(models.Model):
    category_type = models.CharField(max_length=120)
    actif = models.BooleanField(default=True)