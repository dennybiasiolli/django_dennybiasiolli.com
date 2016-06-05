from django.shortcuts import render

def blog_home(request):
    return render(request, 'blog/base.html', {})

def post_list(request):
    return render(request, 'blog/post_list.html', {})
