from django.urls import path
from AppAccount.views import *

urlpatterns = [
    path('mi-cuenta', UserUpdateView.as_view(), name='cuenta'),
    path('mis-publicaciones/crear', CreateCarPost.as_view(), name='crear_publicacion'),
    path('mis-publicaciones', ListCarPost.as_view(), name='mis_publicaciones'),
    path('mis-publicaciones/editar/<int:pk>/', EditCarPost.as_view(), name='editar_publicacion'),
    path('mis-publicaciones/eliminar/<int:pk>/', DeleteCarPost.as_view(), name='borrar_publicacion')
]