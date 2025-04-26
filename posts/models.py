from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=128)  # Short title of the post
    subtitle = models.CharField(max_length=256)  # Subtitle for the post
    body = models.TextField()                 # Full message content
    created_on = models.DateTimeField(auto_now_add=True)  # Auto-set when created

    def __str__(self):
        return self.title  # This will make it easier to identify posts in the admin panel