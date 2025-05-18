from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='blog_image/', null=True, blank=True)
    video = models.FileField(upload_to='blog_video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Blog'
