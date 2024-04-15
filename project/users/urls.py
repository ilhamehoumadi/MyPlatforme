from django.urls import path
from .views import HomeView,ProfileView , MyLoginView,RegisterView
from .views import custom_logout 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Ajoutez vos patterns d'URL ici
    path('home/', HomeView.as_view() , name="home"),
    path('profile/', ProfileView.as_view() , name="profile"),
    path('login/', MyLoginView.as_view() , name="login"),
    path('register/', RegisterView.as_view() , name="register"),
    path('logout/', custom_logout, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)