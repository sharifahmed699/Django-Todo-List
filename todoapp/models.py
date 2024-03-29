from django.db import models

# Create your models here.

class TodoApp(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.title
    
