from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    is_donor = models.BooleanField(default=False)
    is_association = models.BooleanField(default=False)
    

    def __str__(self):
        return self.username


class Profile(models.Model):
    # chaque user a un profile unique + si on supprime user , le profile sera supprimer également
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    
    avatar=models.ImageField(
        default='avatar.jpg',
        upload_to = 'profile_avatar'
    )
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.avatar.path) # Open an image file
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)