from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from KgBlog.models import Post
from django.urls import reverse


def index(request):

    return render(request, 'index.html')





