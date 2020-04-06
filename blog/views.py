from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Category, Post, Tag, Comment
from datetime import datetime


#def home(request):
 #   if request.method == 'GET':
  #      return HttpResponse('Hi')
class HomeView(View):
    '''home page'''
    def get(self, request):
        category_list  = Category.objects.all()
        post_list= Post.objects.filter(published=True, published_date__lte=datetime.now())
        return render(request, 'blog/post_list.html', {'categories' : category_list,
                                                  'post_list' : post_list
                                                  })
class CategoryView(View):
    '''Вывод статей категорий'''
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {'category': category})
class PostDetailView(View):
    """Вывод полной статьи"""
    def get(self, request, category , slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        return render(request, 'blog/post_detail.html', {'categories' : category_list,
                                                      'post' : post
                                                      })

