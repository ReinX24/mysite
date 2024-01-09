from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    """Form for editing posts."""

    class Meta:
        model = Post
        fields = ("title", "text")
