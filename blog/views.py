from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm, RegistrationForm
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django import views
User = get_user_model()


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    last_5_posts = Post.objects.all()[:5]
    return render(request, 'blog/post_list.html', {'posts':posts,'last_5_posts': last_5_posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, 'blog/post_detail.html', {'post':post, 'comments':comments})

def static_page(request):
    form = CommentForm()
    return render(request, 'blog/static_page.html', {'form':form})

def creat_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('post_detail', pk=form.cleaned_data['post'].pk)
    else:
        form = CommentForm()
    return render(request, 'blog/static_page.html', {'form':form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})

# class LoginClassBasedView(views.generic.edit.FormView):
#     form_class = AuthenticationForm
#     success_url = '/'
#     def form_valid(self, form):
#         user = form.get_user()
#         login(self.request, user)
#         return super().form_valid(form)
#
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login_form.html', {'form':form})

def registration_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                password = form.cleaned_data['password'],
                email = form.cleaned_data['email'],
                username = form.cleaned_data['email'],
            )
            return redirect('/catalog/')

    else:
        form = RegistrationForm()
    return render(request, 'blog/login_form.html', {'form':form})



