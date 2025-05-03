from django.db import models


# Create your models here.
class God(models.Model):
    name_hindi = models.CharField(max_length=100, null=True, blank=True)
    name_english = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='god_image/', null=True, blank=True)
    video = models.FileField(upload_to='god_video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'God'
