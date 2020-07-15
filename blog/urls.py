from django.urls import path
from . import views



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('catalog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('main/', views.static_page),
    path('add-comment-url/', views.creat_comment),
    path('login/', views.login_view),
    path('registration/', views.registration_view),


]