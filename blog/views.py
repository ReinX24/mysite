from django.shortcuts import render


# Create your views here.
def post_list(request):
    """Return a HTML template of our posts."""
    return render(request, "blog/post_list.html", {})
