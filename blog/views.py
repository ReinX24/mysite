from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from blog.forms import PostForm
from blog.models import Post


# Create your views here.
def post_list(request):
    """Return a HTML template of our posts."""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, post_id):
    """Return a page with post details."""
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})


def post_new(request):
    """Post a new article."""

    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.published_date = timezone.now()
            new_post.save()
            return redirect("blog:post_detail", post_id=new_post.id)
    else:
        form = PostForm()

    return render(request, "blog/post_edit.html", {"form": form})


def post_edit(request, post_id):
    """Edit an existing post."""
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        # Update existing Post data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', post_id=post.id)
    else:
        # Get existing Post data
        form = PostForm(instance=post)

    return render(request, "blog/post_edit.html", {"form": form})