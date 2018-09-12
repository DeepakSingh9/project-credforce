# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User,AbstractUser
from django.core.validators import RegexValidator

from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.backends import ModelBackend
from django.utils.translation import ugettext_lazy as _





class Profile(models.Model):

    gender_choices=(('male','MALE'),('female','FEMALE'),('other','OTHER'),)

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, )

    profile_image = models.ImageField(upload_to='profilepic/', blank=True)
    organisation = models.CharField(max_length=100,blank=True,null=True)
    designation = models.CharField(max_length=50,blank=True,null=True)

    followed_by = models.ManyToManyField('self', related_name='follows', symmetrical=False, blank=True, null=True)



    def __str__(self):
        return self.user.username







