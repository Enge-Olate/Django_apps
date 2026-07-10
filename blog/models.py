from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

STATUS_CHOICES = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add = True)    
    status=models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title    
    
    def save(self, *args, **kargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kargs)