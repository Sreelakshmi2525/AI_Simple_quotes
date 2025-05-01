from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    moods = models.JSONField(default=list)  # Store relevant moods as list
    
    def __str__(self):
        return f"{self.author}'s Quote"