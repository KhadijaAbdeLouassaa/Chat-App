from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to= "users_thumbnail",default="images/default_thumbnail.png")
    
    def __str__(self):
        return self.user.username
        

def create_profile(sender,**kwargs):
    if kwargs['created'] :
        UserProfile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile, User)       