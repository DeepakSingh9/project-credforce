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
from django_countries import countries


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


        if userlogin.is_valid() and userregister.is_valid():
            user=userlogin.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile=userregister.save(commit=False)
            profile.user=user
            profile.gender=request.POST['gender']
            profile.save()


            login(request,authenticate(username=userlogin.cleaned_data['username'],password=userlogin.cleaned_data['password']))
            return redirect('profile',pk=user.pk)
        else:
            messages.error(request,'There is some problem with your account ..already a member??try loging in ')


    else:
        userlogin=LoginForm()
        userregister=RegistrationForm()
    return render(request,'dashboard/home.html',{'userlogin':userlogin,'userregister':userregister,})





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
def followto(request):
    if request.method=='POST':
        follow_id=request.POST['follow',False]
        if follow_id:
            try:
                user=User.objects.get(id=follow_id)
                request.user.profile.follows.add(user.profile)
            except ObjectDoesNotExist:
                return redirect('/')
    return redirect('/')



@login_required()
def follow(request,pk):
    author=get_object_or_404(User,id=pk)
    user=request.user
    if user.is_authenticated():
        if user.id != get_object_or_404(User,id=pk):
            try:
                author.profile.followed_by.add(user.profile)
                following = True
                return redirect('account',pk=author.id)
            except ObjectDoesNotExist:
                return HttpResponse('The author you are following has removed the account')

    return redirect(request,'/',{})




@login_required()
def account(request,pk):
    user=get_object_or_404(User,pk=pk)
    profile=get_object_or_404(Profile,pk=pk)
    return render(request,'blog/account.html',{'profile':profile,'user':user,})

