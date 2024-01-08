from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog import views

app_name = "blog"
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:post_id>", views.post_detail, name="post_detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
