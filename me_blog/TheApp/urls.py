from . import views
from django.urls import path

# template URLs
app_name = 'TheApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/remove', views.comment_remove, name='comment_remove'),
    path('<str:user.username>/', views.PostListView.as_view(), name='post_list')


]
