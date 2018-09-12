# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post,Like,Category,SmallPost
from .forms import PostUploadForm,CommentForm,SmallPostForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test,login_required




def post_list(request):
    topuser=User.objects.all().exclude(is_superuser=True)[:3]
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:6]
    return render(request, 'blog/post_list.html', {'posts':posts,'topuser':topuser})




def post_detail(request,slug,pk):
    post=get_object_or_404(Post,slug=slug,pk=pk)

    return render(request,'blog/complete_post.html',{'post':post,})


def post_new(request):
    if request.method == "POST":
        form = PostUploadForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug,pk=post.pk)
    else:
        form = PostUploadForm()
    return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request,slug,pk):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostUploadForm(request.POST,request.FILES,instance=post,)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.image = request.FILES('file')
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug, pk=post.pk)
    else:
        form = PostUploadForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required()
def profile(request,pk):
    profile_owner=get_object_or_404(User,pk=pk)
    viewer=request.user
    categories=Category.objects.all()
    followers=profile_owner.profile.followed_by.all()[:6]
    alluser=User.objects.all().exclude(is_superuser=True)[:4]
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    if profile_owner != viewer :
        return redirect('account',pk=viewer.pk)
    else:
        return render(request,'blog/profile.html',{'profile_owner':profile_owner,'posts':posts,'alluser':alluser,'followers':followers,'categories':categories})


@login_required()
def comment(request,pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        commentform=CommentForm(request.POST)
        if commentform.is_valid():
            commentform=commentform.save(commit=False)
            commentform.post=post
            commentform.save()
            return redirect('post_detail',pk=pk, slug=post.slug)
        else:
            return HttpResponse('comment correctly')
    else:
        commentform=CommentForm()
    return render(request,'blog/complete_post.html',{'commentform':commentform})





def Clap(request,pk):
    user=request.user
    post=get_object_or_404(Post,pk)


@login_required()
def small_post(request):
    user=request.user
    if request.method=='POST':
        form=SmallPostForm(request.POST)
        if form.is_valid:
            smallpost=form.save(commit=False)
            smallpost.writer=user
            smallpost.created_date=timezone.now()
            smallpost.save()
            return redirect('profile',pk=user.pk)
    else:
        form=SmallPostForm()
    return render(request,'blog/profile.html',{'form':form})


def about_us(request):
    return render(request,'blog/AboutUs.html',{})


def privacy_policy(request):
    return render(request,'blog/privacypolicy.html',{})

def terms_and_conditions(request):
    return render(request,'blog/terms.html',{})


def blog_published(request,pk):
    profile_owner=get_object_or_404(User,pk=pk)
    viewer=request.user
    categories=Category.objects.all()
    followers=profile_owner.profile.followed_by.all()[:6]
    alluser=User.objects.all().exclude(is_superuser=True)[:4]
    posts=User.objects.get(pk=pk).post_set.all()
    return render(request,'blog/blog_published.html',{'profile_owner':profile_owner,'posts':posts,'alluser':alluser,'followers':followers,'categories':categories})

