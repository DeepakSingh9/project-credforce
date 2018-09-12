# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm,LoginForm,ImageUpload,Follow
from django.contrib.auth.decorators import login_required
from .models import Profile
from blog.models import Post
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone



# Create your views here.

def user_login(request):
    if request.method=='POST':
        userlogin=LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active :
                login(request,user)
                return redirect('profile',pk=user.pk)
            else:
                messages.error(request,'Your account has been removed')
        else:
            return HttpResponse('wrong email id password')

    else:
        userlogin=LoginForm()
    return render(request,'registration/login.html',{'userlogin':userlogin})



def user_registration(request):
    if request.method=='POST':


        userlogin=LoginForm(request.POST)
        userregister=RegistrationForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']

        if userlogin.is_valid() and userregister.is_valid():
            user=userlogin.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile=userregister.save(commit=False)
            profile.user=user
            profile.save()


            login(request,authenticate(username=userlogin.cleaned_data['username'],password=userlogin.cleaned_data['password']))
            return redirect('profile',pk=user.pk)
        else:
            messages.error(request,'there is a problem with your account')

    else:
        userlogin=LoginForm()
        userregister=RegistrationForm()
    return render(request,'blog/post_list.html',{'userlogin':userlogin,'userregister':userregister,})





@login_required()
def user_logout(request):
    logout(request)
    return redirect('/')




@login_required()
def profile_image_upload(request):
    image=False
    user=request.user
    profile = get_object_or_404(Profile, pk=user.id)
    if request.method =='POST':
        form = ImageUpload(request.POST,request.FILES)
        if form.is_valid():
            profile.profile_image=request.FILES['file']
            form.save()
            profile.save()
            image=True
            return redirect('/')
        else:
            return HttpResponse('please choose an images')
    else:
        form=ImageUpload()
    return render(request,'registration/imageupload.html',{'form':form,'profile':profile,'user':user,'images':image})




def dashboard(request):
    post=Post.objects.all()
    user=request.user
    return render(request,'registration/account.html',{'post':post,'user':user})





@login_required()
def follow(request,pk):
    author=get_object_or_404(User,id=pk)
    viewer=request.user
    if viewer.is_authenticated():
        if viewer.id != author.id:
            author.profile.followed_by.add(viewer.profile)
            return redirect('account',pk=author.id)
    return redirect('account',pk=author.id)




@login_required()
def unfollow(request,pk):
    author = get_object_or_404(User, id=pk)
    viewer = request.user
    if viewer.is_authenticated():
        author.profile.followed_by.remove(viewer.profile)
        return redirect('account',pk=author.id)
    return redirect('account',pk=author.id)




@login_required()
def account(request,pk):
    profile_user=get_object_or_404(User,pk=pk)
    viewer=request.user
    followers=profile_user.profile.followed_by.all()[:6]
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    return render(request,'blog/account.html',{'viewer':viewer,'profile_user':profile_user,'posts':posts,'followers':followers})

