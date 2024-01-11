from django import forms

from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    """Form for editing posts."""

    class Meta:
        model = Post
        fields = ("title", "text")


class CommentForm(forms.ModelForm):
    """Form for adding comments to posts."""

    class Meta:
        model = Comment
        fields = ("author", "text")
