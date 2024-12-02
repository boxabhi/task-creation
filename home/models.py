from django.db import models
from django.contrib.auth.models import User
import uuid



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    task_name = models.CharField(max_length=255)
    priority_level = models.CharField(max_length=255, choices=(
        ('Low', 'Low'),('Medium', 'Medium'),('High', 'High')), default="")
    due_date = models.DateField(null=True ,blank=True)
    index = models.IntegerField(default=0)
    