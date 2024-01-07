from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    """Post model that will be stored in our database."""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Publishes our post and sets published_date."""
        self.published_date = timezone.now()
        self.save()  # saving our model to our database

    def __str__(self):
        """String representation of our model, returns title."""
        return self.title
