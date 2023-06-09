from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    path('create-user/', views.UserCreate.as_view(), name='create-user'),
    path('update-user/', views.UserGetSet.as_view(), name='update-user'),
    path('create-comment-user/<int:pk>/', views.CommentCreateUser.as_view(), name='create-comment-user'),
    path('create-comment-property/<int:pk>/', views.CommentCreateProperty.as_view(), name='create-comment-property'),
    path('view-comment-user/<int:pk>/', views.CommentListUser.as_view(), name='view-comment-user'),
    path('view-comment-property/<int:pk>/', views.CommentListProperty.as_view(), name='view-comment-property'),
]
