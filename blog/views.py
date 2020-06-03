from django.shortcuts import render, redirect
from django.utils import timezone
from .models import BlogList
from .forms import NewBlogForm

# Get the time of when the user opens homepage of website
visit_hours = int(timezone.now().time().strftime("%H"))
visit_minutes = int(timezone.now().time().strftime("%M"))
visit_minutes_total = visit_hours * 60 + visit_minutes
print(visit_minutes_total)


def home(request):
    return render(request, "blog/home.html")


def blogs(request):
    blog_set = reversed(BlogList.objects.get(name="Technology").blog_set.all())
    return render(request, "blog/blogs.html", {"blog_set": blog_set})


def create_blog(request):
    global visit_hours, visit_minutes, visit_minutes_total

    # Get the current time and the time difference
    current_hours = int(timezone.now().time().strftime("%H"))
    current_minutes = int(timezone.now().time().strftime("%M"))
    current_minutes_total = current_hours * 60 + current_minutes
    time_diff = current_minutes_total - visit_minutes_total

    # TODO: Remove the below line before commiting
    print(current_minutes_total, visit_minutes_total)

    if request.method == "POST":
        form = NewBlogForm(request.POST)

        # Check if form is valid
        if form.is_valid():
            # Get the relevant blog list
            blog_list = BlogList.objects.get(
                name=form.cleaned_data["blog_list"]
            )

            # Get the information from the form
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            creation_date = form.cleaned_data["creation_date"]
            content = form.cleaned_data["content"]

            # Create the Blog and save it
            b = blog_list.blog_set.create(
                title=title,
                author=author,
                creation_date=creation_date,
                content=content
            )
            b.save()

            # Reset Visit Minutes to current time
            visit_hours = current_hours
            visit_minutes = current_minutes
            visit_minutes_total = visit_hours * 60 + visit_minutes

            return redirect("/blogs")

    else:
        form = NewBlogForm()

    context = {
        "form": form,
        "time_diff": time_diff,
        "time_left": 5 - time_diff
    }
    return render(request, "blog/create.html", context)
