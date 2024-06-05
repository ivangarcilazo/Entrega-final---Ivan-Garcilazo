from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.views.generic.edit import FormView 
from django.urls import reverse_lazy
from AppAuth.form import *
from django.contrib.auth import login,logout
from django.shortcuts import redirect

# Create your models here.
class LoginAppView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('Inicio')
    def get_success_url(self):
        return reverse_lazy('Inicio')
    
class RegisterAppView(FormView):
    template_name = 'register.html'
    form_class = FormCreateUser
    redirect_authenticated_user = True
    success_url = reverse_lazy('Inicio')
    def form_valid(self, form) -> HttpResponse:
        user = form.save()
        if user:
            login(self.request, user)
        return super().form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('Inicio'))
        return super().get(self.request)
    
def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('Inicio'))