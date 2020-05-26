from django import forms
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', 'post')

    def save(self, commit=True):
        comment = Comment(
            author = self.cleaned_data['author'],
            text = self.cleaned_data['text'],
            post = self.cleaned_data['post']
        )
        comment.save()


    # text = forms.CharField(label="Text comment:", max_length=250)
    # page = forms.IntegerField(label="Id page:")

    # def clean_page(self):
    #     page_id = self.cleaned_data['page']
    #
    #     if not Post.objects.filter(pk=page_id).exists():
    #         raise forms.ValidationError("Page with id = s% doesn't exist" % page_id)
    #     return page_id

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'email']

