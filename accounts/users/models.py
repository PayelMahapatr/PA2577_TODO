from django.db import models
import uuid


# Create your models here.
class Customer(models.Model):
    """Model for Guest's details for the profile."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    

    class Meta:
        managed = True
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    
