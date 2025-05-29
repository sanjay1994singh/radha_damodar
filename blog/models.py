from django.db import models


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='blog_image/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'BlogCategory'


class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='blog_image/', null=True, blank=True)
    video = models.FileField(upload_to='blog_video/', null=True, blank=True)
    views = models.IntegerField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Blog'


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    desc = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.blog)

    class Meta:
        db_table = 'BlogComment'
