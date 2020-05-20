from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.Form):
    text = forms.CharField(max_length=250)
    page = forms.IntegerField()

