from django.db import models


# Create your models here.
class DarshanTime(models.Model):
    season = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='owner_video/', null=True, blank=True)
    from_time = models.TimeField(null=True, blank=True)
    to_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'DarshanTime'
