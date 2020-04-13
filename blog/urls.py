from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_name>/', views.CategoryView.as_view(), name='category'),
    path('', views.CategoryView.as_view()),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name='detail_post'),
    path('tag/<slug:slug>/', views.CategoryView.as_view(), name='tag')
]