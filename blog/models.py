from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING) #(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    # text = models.TextField()
    # author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # created = models.DateTimeField(auto_created=True, null=True, blank=True)
    # page = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return "%s - %s - %s - " % (self.author.pk, self.pk, self.text)

# Create your models here.
