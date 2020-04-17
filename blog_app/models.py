from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='post_author')
    creation_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()