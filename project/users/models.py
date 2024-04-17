from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission



# Create your models here.

class Donor(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields specific to UserType1
    occupation = models.CharField(max_length=100)

    # Add any other fields specific to UserType1
    groups = models.ManyToManyField(Group, related_name='donor_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='donor_user_permissions',
        blank=True
    )

class Association(AbstractUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields specific to UserType2
    organisation = models.CharField(max_length=100)
    
    # Add any other fields specific to UserType2
    groups = models.ManyToManyField(Group, related_name='association_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='association_user_permissions',
        blank=True
    )



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