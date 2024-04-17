from django.contrib import admin
from .models import Profile
#from django.contrib.auth.admin import UserAdmin
#from .models import CustomUser
from .models import Donor, Association

# on ajout ici tous ce qu'on peut afficher dans page administration de django
#admin.site.register(CustomUser)
admin.site.register(Donor)
admin.site.register(Association)
admin.site.register(Profile)
