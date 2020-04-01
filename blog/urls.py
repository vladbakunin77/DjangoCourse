from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_name>/', views.CategoryView.as_view(), name='category'),
    path('', views.HomeView.as_view()),
    path('<slug:post_slug>/', views.PostView.as_view(), name='post_detail')
]