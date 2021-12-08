from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add),
    path('edit/<int:tweet_id>/', views.edit),
    path('delete/<int:tweet_id>/', views.delete),
    path('like/<int:tweet_id>/', views.LikeView, name='like_post'),
]
