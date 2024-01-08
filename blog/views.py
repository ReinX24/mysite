from django.shortcuts import get_object_or_404, render
from django.utils import timezone
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
