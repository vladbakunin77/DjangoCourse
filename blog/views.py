from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Category, Post, Tag, Comment



#def home(request):
 #   if request.method == 'GET':
  #      return HttpResponse('Hi')
class HomeView(View):
    '''home page'''
    def get(self, request):
        category_list  = Category.objects.all()
        posts_list= Post.objects.all()
        return render(request, 'blog/home.html', {'categories' : category_list,
                                                  'post' : posts_list
                                                  })
    def post(self, request):
        pass
class CategoryView(View):
    '''Вывод статей категорий'''
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {'category': category})
class PostView(View):
    '''Вывод отдельного поста'''
    def get(self, request, post_slug):
        post_lists = Post.objects.get(slug=post_slug)
        return render(request,'blog/post.html',{'posts' : post_lists})

