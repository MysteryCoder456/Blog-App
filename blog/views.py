from django.shortcuts import render, redirect
from .models import BlogList
from .forms import NewBlogForm


def home(request):
    return render(request, "blog/home.html")


def blogs(request):
    blog_set = reversed(BlogList.objects.get(name="Technology").blog_set.all())
    return render(request, "blog/blogs.html", {"blog_set": blog_set})


def create_blog(request):
    if request.method == "POST":
        form = NewBlogForm(request.POST)

        if form.is_valid():
            blog_list = BlogList.objects.get(name=form.cleaned_data["blog_list"])
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            creation_date = form.cleaned_data["creation_date"]
            content = form.cleaned_data["content"]

            b = blog_list.blog_set.create(
                title=title,
                author=author,
                creation_date=creation_date,
                content=content
            )
            b.save()

    else:
        form = NewBlogForm()

    return render(request, "blog/create.html", {"form": form})
