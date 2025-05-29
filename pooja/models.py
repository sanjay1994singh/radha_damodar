from django.db import models


# Create your models here.
class PoojaCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'PoojaCategory'


class Pooja(models.Model):
    category = models.ForeignKey(PoojaCategory, on_delete=models.CASCADE, null=True, blank=True)
    name_hindi = models.CharField(max_length=100, null=True, blank=True)
    name_english = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='pooja_image/', null=True, blank=True)
    video = models.FileField(upload_to='pooja_video/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name_hindi) + str(self.name_english)

    class Meta:
        db_table = 'Pooja'
