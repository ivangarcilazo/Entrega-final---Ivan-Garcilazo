from django.contrib.auth import authenticate, update_session_auth_hash
from django.db.models.query import QuerySet
from django.views.generic.edit import UpdateView,CreateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from AppAccount.models import *

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    context_object_name = 'user'
    template_name = 'edit_user.html'
    fields = ['username', 'email']
    success_url = reverse_lazy('cuenta')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  

        password_old_exist = len(request.POST.get('password_old')) > 0
        password_exist = len(request.POST.get('password')) > 0
        
        if password_old_exist and password_exist:
            old_password = request.POST.get('password_old')
            new_password = request.POST.get('password')

            if not authenticate(username=self.object.username, password=old_password):
                messages.error(request, 'La contraseña antigua no es correcta.')
                
                form = self.get_form()
                return self.form_invalid(form)
            else:                
                self.object.set_password(new_password)
                self.object.save()
                update_session_auth_hash(request, self.object)
                messages.success(request, 'Tu contraseña ha sido actualizada con éxito.')

        return super().post(request, *args, **kwargs)

class CreateCarPost(LoginRequiredMixin, CreateView):
    model = CarPosts
    template_name='account_create_car.html'
    fields = ['title','price','image','description']
    success_url = reverse_lazy('mis_publicaciones')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ListCarPost(LoginRequiredMixin, ListView):
    model = CarPosts
    template_name='account_car.html'
    context_object_name = 'car_posts'
    def get_queryset(self) -> QuerySet:
        return CarPosts.objects.filter(user_id=self.request.user)

class EditCarPost(LoginRequiredMixin, UpdateView):
    model=CarPosts
    template_name='account_edit_car.html'
    fields=['title','price','image','description']
    success_url = reverse_lazy('mis_publicaciones')
    def get_queryset(self) -> QuerySet:
        return CarPosts.objects.filter(user=self.request.user)
    
class DeleteCarPost(LoginRequiredMixin, DeleteView):
    model = CarPosts
    template_name = 'account_confirm_delete_car.html'
    context_object_name='car'
    success_url = reverse_lazy('mis_publicaciones')
    
    def get_queryset(self):
        return CarPosts.objects.filter(user=self.request.user)
    