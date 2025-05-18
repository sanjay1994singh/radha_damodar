from django.db import models


# Create your models here.
class DailyDarshan(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='owner_image/', null=True, blank=True)
    video = models.FileField(upload_to='owner_video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Daily_Darshan'
