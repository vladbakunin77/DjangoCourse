from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Category, Post, Tag, Comment
from datetime import datetime


#def home(request):
 #   if request.method == 'GET':
  #      return HttpResponse('Hi')
#class HomeView(View):
 #   '''home page'''
  #  def get(self, request):
   #     category_list  = Category.objects.all()
    #    post_list= Post.objects.filter(published=True, published_date__lte=datetime.now())
     #   return render(request, 'blog/post_list.html', {'categories' : category_list, 'post_list' : post_list})

class CategoryView(View):
    '''Вывод статей категорий'''
    def get_querryset(self):
        return Post.objects.filter(published=True, published_date__lte=datetime.now())
    def get(self, request, category_slug=None, slug=None):
        category_list = Category.objects.filter(published=True)
        if category_slug is not None:
            posts = self.get_querryset().filter(category__slug=category_slug, category__published=True,published=True)
        elif slug is not None:
            posts = self.get_querryset().filter(tags__slug=slug, tags__published=True)
        else:
            posts = self.get_querryset()
        if posts.exists():
            template = posts.first().get_category_template()
        else:
            template = 'blog/post_list.html'
        return render(request, template, {'post_list': posts, 'categories' : category_list,})

class PostDetailView(View):
    """Вывод полной статьи"""
    def get(self, request, **kwargs):
        category_list = Category.objects.all()
        post = get_object_or_404(Post, slug=kwargs.get('slug'))
        return render(request, post.template, {'categories' : category_list, 'post' : post,})

#class TagView(View):
 #   def get(self, request, slug):
  #      posts = Post.objects.filter(tags__slug=slug, published=True)
   #     return render(request, posts.firs().get_category_template(), {'post_list': posts})