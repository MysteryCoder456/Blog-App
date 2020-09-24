import math
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import *
from .forms import BlogSortForm, NewBlogForm, NewCommentForm
# Get the time of when the user opens homepage of website
visit_hours = int(timezone.now().time().strftime("%H"))
visit_minutes = int(timezone.now().time().strftime("%M"))
visit_minutes_total = visit_hours * 60 + visit_minutes


def reset_visit_time(current_time):
    global visit_hours, visit_minutes, visit_minutes_total
    visit_hours = current_time[0]
    visit_minutes = current_time[1]
    visit_minutes_total = visit_hours * 60 + visit_minutes


# Views

# LABEL: HOME PAGE
def home(request):
    bday_days = 25 + 9 * 30 + 2006 * 365

    print(timezone.now().date().isoformat())
    current_years = int(timezone.now().date().isoformat()[0:4])
    current_months = int(timezone.now().date().isoformat()[6:7])
    current_days = int(timezone.now().date().isoformat()[8:10])
    current_total_days = current_days + current_months * 30 + current_years * 365

    age = math.floor((current_total_days - bday_days) / 365)
    return render(request, "blog/home.html", {"age": age})


# LABEL: VIEWS BLOGS
def blogs(request):
    all_blogs = []

    for blog_list in BlogList.objects.all():
        if blog_list.name != "Dev Logs":
            all_blogs.extend(blog_list.blog_set.all())

    all_blogs.sort(key=lambda blog: blog.creation_date, reverse=True)
    return render(request, "blog/blogs.html", {"blog_set": all_blogs})


# LABEL: BLOG DETAIL
@login_required
def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    user_id = request.user.id
    user_check = {"user_id": user_id}
    user_votes_up = blog.votes.user_ids(0)
    user_votes_down = blog.votes.user_ids(1)
    action = 0

    # Get blog's comments
    comment_set = list(blog.comment_set.all())
    comment_set.sort(key=lambda comment: comment.creation_date, reverse=True)

    if request.method == "POST":
        vote = request.POST.get("vote")
        comment_form = NewCommentForm(request.POST)

        if vote == "upvote":
            blog.votes.up(user_id)
        elif vote == "downvote":
            blog.votes.down(user_id)

        if comment_form.is_valid():
            comment_author = request.user.username
            comment_content = comment_form.cleaned_data["content"]
            comment_creation_date = timezone.localdate()

            blog.comment_set.create(
                author=comment_author,
                creation_date=comment_creation_date,
                content=comment_content
            )

        blog.save()
    else:
        comment_form = NewCommentForm()

    if user_check in user_votes_up.values('user_id'):
        action = 1
    elif user_check in user_votes_down.values('user_id'):
        action = -1

    context = {
        "blog": blog,
        "action": action,
        "points": blog.votes.count(),
        "comment_set": comment_set,
        "comment_count": len(comment_set),
        "comment_form": comment_form
    }
    return render(request, "blog/blog_detail.html", context)


# LABEL: CREATE BLOG
@login_required
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
            author = request.user.username
            creation_date = timezone.localdate()
            content = form.cleaned_data["content"]

            # Create the Blog and save it
            b = blog_list.blog_set.create(
                title=title,
                author=author,
                creation_date=creation_date,
                content=content
            )
            b.save()

            # Reset Visit Minutes to current time and alert
            reset_visit_time((current_hours, current_minutes))
            messages.success(
                request, f"Blog {title} successfully created by {author}!")

            return redirect("new_blogs")

    else:
        form = NewBlogForm()

    context = {
        "form": form,
        "time_diff": time_diff,
        "time_left": 5 - time_diff
    }
    return render(request, "blog/create.html", context)


# LABEL: DEV LOGS
def dev_logs(request):
    dev_set = reversed(BlogList.objects.get(name="Dev Logs").blog_set.all())
    return render(request, "blog/dev.html", {"dev_set": dev_set})


# LABEL: CATEGORIES
def categories(request):
    if request.method == "POST":
        form = BlogSortForm(request.POST)

        if form.is_valid():
            list_name = request.POST.get("category")
            blog_list = BlogList.objects.get(name=list_name)
            blog_set = blog_list.blog_set.all()
            if len(blog_set) < 1:
                messages.warning(
                    request, "There are no blogs in this categories yet!")

    else:
        blog_set = []
        form = BlogSortForm()

    context = {
        "form": form,
        "blog_set": blog_set
    }
    return render(request, "blog/categories.html", context)
