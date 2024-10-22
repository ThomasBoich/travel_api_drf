from django.db import models
from users.models import CustomUser
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='blog/posts/images/%Y/%m/%d/')
    text = models.TextField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    public_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    likes = models.ManyToManyField(CustomUser, blank=True, null=True, related_name='likes')
    views = models.ManyToManyField(CustomUser, blank=True, null=True, related_name='views')
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
    public_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Category(models.Model):
    name = models.CharField(max_length=249, blank=True, null=True)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'