from django.db import models

class Task(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'pending'),
        ('IN PROGRESS', 'in progress'),
        ('COMPLETED', 'completed')
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='')
    due_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
