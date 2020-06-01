from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogList
from .forms import NewBlogForm


def home(request):
    return render(request, "blog/home.html")


def blogs(request):
    bl = BlogList.objects.get(name="Technology")
    return render(request, "blog/blogs.html", {"bloglist": bl})


def create_blog(request):
    if request.method == "POST":
        form = NewBlogForm(request.POST)

    else:
        form = NewBlogForm()

    return render(request, "blog/create.html", {"form": form})
