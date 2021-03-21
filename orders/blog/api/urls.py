

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/<pk>', views.PostDetailsView.as_view(), name='post_detail'),
]