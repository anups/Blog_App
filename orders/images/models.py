from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


# ======================================================================================================
# One to Many association : A user can post multiple images but each image is posted by a single user
# ManyToMany relationship : When you define Django creates an intermediary join table using primary key
#                           of both the models.
#                           1. image.users_like.all()
#                           2. user.images_liked.all()
# ======================================================================================================


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)  # One to Many association
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)
    created = models.DateField(auto_now_add=True,
                               db_index=True)  # Creates an index table

    def __str__(self):
        return self.title

    # Use the slugify() method of Django to automatically generate the image slug
    # for the given title when no slug is provided
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('image:detail',
                       args=[self.id, self.slug])

