from django.urls import path
from AppKinda.views import *

urlpatterns = [
    path('acerca-de-mi', AboutMeView.as_view(), name='Acerca de mi' ),
    path('', IndexView.as_view(), name='Inicio'),
    path('inicio/publicacion/<int:pk>', PostDetailView.as_view(), name='detalle_publicacion'),
    path('inicio/publicacion/comment', addComment, name='anadir_comentario_publicacion')
]