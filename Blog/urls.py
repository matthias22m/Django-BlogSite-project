from django.urls import path,include
from .views import PostListView,PostDetailView
from . import views

urlpatterns = [
    path("", PostListView.as_view() , name="blogs_all"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
]

