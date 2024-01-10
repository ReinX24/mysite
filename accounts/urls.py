from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from blog import views

app_name = "accounts"
urlpatterns = [path("", include("django.contrib.auth.urls"))]
