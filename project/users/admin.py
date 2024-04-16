from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin
from .models import User
# on ajout ici tous ce qu'on peut afficher dans page administration de django

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
