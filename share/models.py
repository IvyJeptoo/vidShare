from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    photo = CloudinaryField('image',default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    bio = models.CharField(max_length=300) 
        
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
            
            
    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def profile(cls):
        profiles = cls.objects.all()
        return profiles

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
    
    def __str__(self):
        return self.user.username