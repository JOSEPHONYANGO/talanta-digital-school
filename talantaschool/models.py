
from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username =  models.CharField(max_length=100)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=250)    
    mobile_number = models.IntegerField(blank=True, null=True)
    email =  models.CharField(max_length=60) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)    

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()  