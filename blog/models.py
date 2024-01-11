from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    """Post model for storing information in our database."""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Set published_date and save Post to database."""
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        """Return approved_comments."""
        return self.comment_set.filter(approved_comment=True)

    def __str__(self):
        """String representation of our Post model."""
        return self.title


class Comment(models.Model):
    """Comment model for storing information regarding comments for posts."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=128)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        """Changes approved_comment to True and saves comment to database."""
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
