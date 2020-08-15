from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blog(request):
    blogs = Blog.objects.all()
    allblogData = {'blogs':blogs}
    return render(request, 'blog/all_blog.html', allblogData)


def view_blog(request, bid):
    view_blog = get_object_or_404(Blog, pk=bid)
    viewblogData = {'view_blog':view_blog}
    return render(request, 'blog/view_blog.html', viewblogData)