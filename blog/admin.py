from django.contrib import admin

from .models import Blog, BlogCategory, BlogComment


# Register your models here.
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'id']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'img', 'id']


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'id']


admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
