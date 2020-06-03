from django.shortcuts import render, redirect
from django.utils import timezone
from .models import BlogList
from .forms import NewBlogForm

# Get the time of when the user opens homepage of website
visit_time = int(timezone.now().time().strftime("%M"))
print(visit_time)


def home(request):
    return render(request, "blog/home.html")


def blogs(request):
    blog_set = reversed(BlogList.objects.get(name="Technology").blog_set.all())
    return render(request, "blog/blogs.html", {"blog_set": blog_set})


def create_blog(request):
    global visit_time

    # Get the current time and the time difference
    current_time = int(timezone.now().time().strftime("%M"))
    time_diff = current_time - visit_time

    print(current_time, visit_time)

    if request.method == "POST":
        form = NewBlogForm(request.POST)

        if form.is_valid():
            blog_list = BlogList.objects.get(
                name=form.cleaned_data["blog_list"]
            )

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

            visit_time = int(timezone.now().time().strftime("%M"))
            return redirect("/blogs")

    else:
        form = NewBlogForm()

    context = {
        "form": form,
        "time_diff": time_diff,
        "time_left": 5 - time_diff
    }
    return render(request, "blog/create.html", context)
