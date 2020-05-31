from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogList


def home(request):
    return render(request, "blog/home.html")


def blogs(request):
    bl = BlogList.objects.get(name="Technology")
    return render(request, "blog/blogs.html", {"bloglist": bl})
