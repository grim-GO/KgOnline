from django.conf.urls import url
from django.views.generic import ListView, DetailView
from KgBlog.models import Post
from . import views


urlpatterns = [

    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("pub_date")[:100],
    template_name="posts.html")),

]