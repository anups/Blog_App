from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
    )

    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)  # Dates will be saved automatically when you create the record
    updated = models.DateTimeField(auto_now=True)  # Dates will be updated automatically when you updated the record
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
# Create your models here.
