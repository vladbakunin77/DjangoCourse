from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.utils import timezone
from django.urls import reverse

class Category(MPTTModel):
    '''Модель категорий'''
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField("Url", max_length=100)
    description = models.TextField('Описание', max_length=100, default='', blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural='Категории'
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    template = models.CharField('Шаблон', max_length=100, default='blog/post_list.html')
    published = models.BooleanField('Отображать?', default=True)
    paginated = models.PositiveIntegerField('Колличество новостей на странице', default=5)
    sort = models.PositiveIntegerField('Порядок', default=0)
class Tag(models.Model):
    '''Модель тэгов'''
    name = models.CharField(verbose_name='Тэг', max_length=100)
    slug = models.SlugField(verbose_name='url', max_length=100)
    published = models.BooleanField('Отображать?', default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Тэг'
        verbose_name_plural='Тэги'
class Post(models.Model):
    '''Модель постов'''
    title = models.CharField(verbose_name='Заголовок',max_length=100)
    mini_text = models.TextField(verbose_name='Текст',max_length=100)
    text = models.TextField(verbose_name='Основной текст', max_length=500)
    created_date = models.DateTimeField(verbose_name='Дата создания',max_length=50, auto_now_add=True)
    slug = models.SlugField(verbose_name='Url', max_length=100)
    subtitle = models.CharField('Под заголовок', max_length=100, blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'
    tags = models.ManyToManyField(Tag, verbose_name='Тэг', blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete = models.CASCADE,
        null=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    published_date = models.DateTimeField(
        'Дата публикации',
        default=timezone.now,
        blank=True,
        null=True,
    )
    edit_date = models.DateTimeField(
        'Дата изменения',
        default=timezone.now,
        blank=True,
        null=True,
    )
    template = models.CharField('Шаблон', max_length=500, default='blog/post_detail.html')
    image = models.ImageField('Главная фотография', upload_to='post/', null=True, blank=True)
    published = models.BooleanField('Опубликовать?',default=True)
    viewed = models.PositiveIntegerField('Просмотрено', default=0)
    status = models.BooleanField('Для зарегестрированных', default=False)
    sort = models.PositiveIntegerField('порядок', default=0)
    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'category':self.category.slug,'slug':self.slug})
    def get_tags(self):
        return self.tags.all()
    def get_comments_count(self):
        return self.comments.count()

class Comment(models.Model):
    '''Модель комментариев'''
    text = models.TextField(verbose_name='Текст',max_length=100)
    created_date = models.DateTimeField(verbose_name='Дата создания', max_length=50)
    moderation = models.BooleanField(verbose_name='Управление',max_length=2)
    def __str__(self):
        return self.text
    post = models.ForeignKey(
        Post,
        verbose_name='Статья',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete= models.CASCADE,
    )