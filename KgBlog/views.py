from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from KgBlog.models import Post
from django.urls import reverse
from KgBlog.forms import PostForm
from django.views import View
import datetime

a = datetime.datetime.now()
Post.pub_date = a


def landing(request):
    name = "Post"
    form = PostForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

        new_form = form.save()

    return render(request, 'index.html', locals())









