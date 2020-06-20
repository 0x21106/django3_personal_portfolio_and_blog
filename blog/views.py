from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.order_by('-created')
    return render(request, 'blog/home.html', {'blogs' : blogs})

def blog_detail(request, blogId):
    blog = get_object_or_404(Blog, pk=blogId)
    return render(request, 'blog/detail.html', {'blog' : blog})