from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class FormCreateUser(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario',widget=forms.TextInput(attrs={'class':'py-2 px-1 w-full rounded'}))
    email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'py-2 px-1 w-full rounded'}))
    password1 = forms.CharField(label='Contraseña',max_length=25, widget=forms.TextInput(attrs={'class':'py-2 px-1 w-full rounded'}))
    password2 = forms.CharField(label='Confirme la contraseña', max_length=25, widget=forms.TextInput(attrs={'class':'py-2 px-1 w-full rounded'}) )
    
    class Meta:
        model = User
        fields = ['email','username','password1', 'password2']
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso. Por favor, elige otro.")
        return username
    