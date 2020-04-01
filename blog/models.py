from django.db import models

class Category(models.Model):
    '''Модель категорий'''
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField("Url", max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural='Категории'
class Tag(models.Model):
    name = models.CharField(verbose_name='Тэг', max_length=100)
    slug = models.SlugField(verbose_name='url', max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Тэг'
        verbose_name_plural='Тэги'
class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок',max_length=100)
    mini_text = models.TextField(verbose_name='Текст',max_length=100)
    text = models.TextField(verbose_name='Основной текст', max_length=500)
    created_date = models.DateTimeField(verbose_name='Дата создания',max_length=50)
    slug = models.SlugField(verbose_name='Url', max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'
class Comment(models.Model):
    text = models.TextField(verbose_name='Текст',max_length=100)
    created_date = models.DateTimeField(verbose_name='Дата создания', max_length=50)
    moderation = models.BooleanField(verbose_name='Управление',max_length=2)
    def __str__(self):
        return self.text
