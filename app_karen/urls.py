from django.urls import path

from app_karen import views

urlpatterns = [
    # Karen Post CRUD Views
    path('', views.IndexView.as_view(), name='index'),
    path('post/create/', views.KarenPostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/detail/', views.KarenPostDetailView.as_view(), name='post-detail'),
    path('post/<slug:slug>/update/', views.KarenPostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', views.KarenPostDeleteView.as_view(), name='post-delete'),
    # Comment CRUD Views
    path('post/<slug:slug>/comment/create/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<uuid:uuid>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<uuid:uuid>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
    # Karen Admin CRUD Views
    path('moderate/posts/review/', views.AdminPostsReviewView.as_view(), name='admin-posts-review'),
    path(
        'moderate/post/<slug:slug>/comments/review/',
        views.AdminCommentsReviewView.as_view(),
        name='admin-comments-review'
    ),
]
