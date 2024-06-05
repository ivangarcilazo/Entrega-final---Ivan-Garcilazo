from django.urls import path
from AppAuth.views import *

urlpatterns = [
    path('login', LoginAppView.as_view(), name='Login'),
    path('registro', RegisterAppView.as_view(), name='Registro' ),
    path('logout', logout_user, name='Logout' )
]