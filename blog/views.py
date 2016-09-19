from django.shortcuts import render
from django.utils import timezone

from .models import Post, Work


def blog_home(request):
    return render(request, 'blog/base.html', {})


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def works_list(request):
    works = Work.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/works_list.html', {'works': works})
