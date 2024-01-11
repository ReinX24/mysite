from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog import views

app_name = "blog"
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("post/new/", views.post_new, name="post_new"),
    path("post/<int:post_id>/edit/", views.post_edit, name="post_edit"),
    path("drafts/", views.post_draft_list, name="post_draft_list"),
    path("post/<int:post_id>/publish/", views.post_publish, name="post_publish"),
    path("post/<int:post_id>/remove/", views.post_remove, name="post_remove"),
    path(
        "post/<int:post_id>/comment/",
        views.add_comment_to_post,
        name="add_comment_to_post",
    ),
    path(
        "comment/<int:comment_id>/approve/",
        views.comment_approve,
        name="comment_approve",
    ),
    path(
        "comment/<int:comment_id>/remove/", views.comment_remove, name="comment_remove"
    ),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
