# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile,User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _




# Register your models here.



class ProfileAdmin(admin.ModelAdmin):
    fields=['user','designation','organisation','profile_image','followed_by','gender']


admin.site.register(Profile,ProfileAdmin)


