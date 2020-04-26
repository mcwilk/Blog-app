from django.db import models
from django.utils import timezone

class Post(models.Model):
    CATEGORIES = (
        (1, "django"),
        (2, "backend"),
        (3, "python"),
        (4, "programming"),
        (5, "webdev"),
    )

    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='post_author')
    creation_date = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(null=True, blank=True)
    category1 = models.SmallIntegerField(choices=CATEGORIES, default=1)
    category2 = models.SmallIntegerField(choices=CATEGORIES, null=True, blank=True)
    category3 = models.SmallIntegerField(choices=CATEGORIES, null=True, blank=True)
    counter = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def publish(self):
        self.publication_date = timezone.now()
        self.save()
    
class Comment(models.Model):
    post = models.ForeignKey('blog_app.Post', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comment_author')
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
