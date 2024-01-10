from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from blog.forms import PostForm
from blog.models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
def post_list(request):
    """Return a HTML template of our posts."""
    # __lte: less than or equal to, checks for posts whose published_date is
    # less than or equal to the current date.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, post_id):
    """Return a page with post details."""
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})


@login_required
def post_new(request):
    """Post a new article."""
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            # This will be saved as a draft, the published_date is not set yet
            # which means this will not be seen in the post_list page.
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect("blog:post_detail", post_id=new_post.id)
    else:
        form = PostForm()

    return render(request, "blog/post_new.html", {"form": form})


@login_required
def post_edit(request, post_id):
    """Edit an existing post."""
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        # Update existing Post data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:post_detail", post_id=post.id)
    else:
        # Get existing Post data
        form = PostForm(instance=post)

    return render(request, "blog/post_edit.html", {"form": form, "post": post})


@login_required
def post_draft_list(request):
    """Show page of existing drafts (no publish_date)."""
    draft_posts = Post.objects.filter(published_date__isnull=True).order_by(
        "-created_date"
    )
    return render(request, "blog/post_draft_list.html", {"draft_posts": draft_posts})


@login_required
def post_publish(request, post_id):
    if request.method == "GET":
        post = get_object_or_404(Post, id=post_id)
        post.publish()  # sets publised_date, check models.py for more info.
        return redirect("blog:post_detail", post_id=post_id)


@login_required
def post_remove(request, post_id):
    if request.method == "GET":
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return redirect("blog:post_list")
