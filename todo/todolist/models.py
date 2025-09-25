from django.db import models

# Create your models here.
class Tasks(models.Model):
    """Model for tasks."""

    
    user_id = models.IntegerField()
    task_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        managed = True
        verbose_name = "Tasks"
        verbose_name_plural = "Tasks"
    
    def __str__(self):
        return self.task_description