from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView , FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm
from django.contrib.auth import login,logout
from django.shortcuts import redirect,HttpResponseRedirect


class HomeView(TemplateView):
    template_name = 'users/home.html'

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'users/profile.html'
    # LoginRequiredMixin : pour restreindre l'accès à une vue en utilise 

class MyLoginView(LoginView):
    template_name='users/registration/register.html'
    redirect_authenticated_user= False #login in next time directly

    def get_success_url(self):
        messages.info(self.request, 'Welcome in your profile')
        return reverse_lazy('profile')
    
    def form_invalid(self, form):
        messages.error(self.request, 'error username or password') # keep the error abstract don't specifie
        return self.render_to_response(self.get_context_data(form=form))
        

def custom_logout(request):
    print('Logging out {}'.format(request.user))
    logout(request)
    print(request.user)
    return HttpResponseRedirect('/')  #direction  home




class RegisterView(FormView):
    redirect_authenticated_user = False
    template_name='users/registration/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('profile')

    def dispatch(self,request,*args,**Kwargs):
        #verified that the user are login or not 
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request,*args,**Kwargs)


    def form_valid(self,form):
        user= form.save()
        if user:
            login(self.request,user)
        return super(RegisterView, self).form_valid(form)
