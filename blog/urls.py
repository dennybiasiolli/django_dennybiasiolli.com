from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_home, name='blog_home'),
    url(r'^blog/', views.post_list, name='post_list'),
    url(r'^works/', views.works_list, name='works_list'),
]
