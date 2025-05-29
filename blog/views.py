from django.shortcuts import render

from .models import Blog, BlogComment


# Create your views here.
def details(request, id):
    blog = Blog.objects.get(id=id)
    pre_count = blog.views
    total = pre_count + 1
    blog.views = total
    blog.save()

    comment = BlogComment.objects.filter(blog_id=id)
    comment_count = comment.count()

    context = {
        'id': id,
        'blog': blog,
        'comment': comment,
        'comment_count': comment_count,
    }
    return render(request, 'blog-details.html', context)


def comment(request):
    form = request.POST
    comment = form.get('comment')
    name = form.get('name')
    email = form.get('email')
    blog = Blog.objects.get(id=id)
    pre_count = blog.views
    total = pre_count + 1
    blog.views = total
    blog.save()

    comment = BlogComment.objects.filter(blog_id=id)
    comment_count = comment.count()

    context = {
        'id': id,
        'blog': blog,
        'comment': comment,
        'comment_count': comment_count,
    }
    return render(request, 'blog-details.html', context)
