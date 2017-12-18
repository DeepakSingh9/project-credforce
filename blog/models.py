# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
from tinymce.widgets import TinyMCE
from tinymce import models as t_m
from django.template.defaultfilters import slugify
from django.apps import AppConfig



class Category(models.Model):
    category_name=models.CharField(max_length=128)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural='Categories'




class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = t_m.HTMLField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image=models.FileField(blank=True,upload_to='blogimages/pic',default='/static/images/blankprofile.jpg')
    category=models.ForeignKey(Category,blank=True,null=True,on_delete=models.CASCADE)
    slug=models.SlugField(null=True,blank=True,max_length=500)









    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)




    def publish(self):
        self.published_date = timezone.now()
        self.save()





    def __str__(self):
        return self.title



class Like(models.Model):
    like=models.IntegerField(default=0)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='has_likes')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes')
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.like




class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments' , on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE,related_name='commented_on')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)







class SmallPost(models.Model):
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(max_length=150)
    created_date=models.DateTimeField(auto_now_add=True)











