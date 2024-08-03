
# Create your models here.
from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __init__(self, *args, **kwargs):
        # Custom initialization logic
        super().__init__(*args, **kwargs)
        # Example: Print a message when a Task instance is created
        print(f'Task instance created with title: {self.title}')

    def __str__(self):
        return f'{self.title} ({self.priority})'
