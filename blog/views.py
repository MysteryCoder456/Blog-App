from django.shortcuts import render, redirect
from django.utils import timezone
from .models import BlogList
from .forms import NewBlogForm

# Get the time of when the user opens homepage of website
visit_hours = int(timezone.now().time().strftime("%H"))
visit_minutes = int(timezone.now().time().strftime("%M"))
visit_minutes_total = visit_hours * 60 + visit_minutes
print(visit_minutes_total)


def reset_visit_time(current_time):
    global visit_hours, visit_minutes, visit_minutes_total
    visit_hours = current_time[0]
    visit_minutes = current_time[1]
    visit_minutes_total = visit_hours * 60 + visit_minutes

# Views

# LABEL: HOME PAGE
def home(request):
    return render(request, "blog/home.html")


# LABEL: VIEWS BLOGS
def blogs(request):
    all_blogs = []

    for blog_list in BlogList.objects.all():
        if blog_list.name != "Dev Logs":
            all_blogs.extend(blog_list.blog_set.all())

    all_blogs.sort(key=lambda blog: blog.creation_date, reverse=True)
    return render(request, "blog/blogs.html", {"blog_set": all_blogs})


# LABEL: CREATE BLOG
def create_blog(request):
    global visit_hours, visit_minutes, visit_minutes_total

    # Get the current time and the time difference
    current_hours = int(timezone.now().time().strftime("%H"))
    current_minutes = int(timezone.now().time().strftime("%M"))
    current_minutes_total = current_hours * 60 + current_minutes
    time_diff = current_minutes_total - visit_minutes_total

    # If the current time reaches the next day, reset visit_time
    if current_minutes_total < visit_minutes_total:
        reset_visit_time((current_hours, current_minutes))

    # Handle form input
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
            reset_visit_time((current_hours, current_minutes))

            return redirect("/blogs")

    else:
        form = NewBlogForm()

    context = {
        "form": form,
        "time_diff": time_diff,
        "time_left": 5 - time_diff
    }
    return render(request, "blog/create.html", context)


def dev_logs(request):
    dev_set = reversed(BlogList.objects.get(name="Dev Logs").blog_set.all())
    return render(request, "blog/dev.html", {"dev_set": dev_set})
