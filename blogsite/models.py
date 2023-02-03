from django.db import models
from django.urls import reverse


# Create your models here.
class Myblog(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('blog_post', args=[self.slug])
