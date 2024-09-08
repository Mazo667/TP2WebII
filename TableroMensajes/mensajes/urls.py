from django.urls import path
from .views import MensajeCreateView, MensajeDeleteView, MensajeListView, MensajeDetailView, MensajeListViewByUser, index, mensajeCreated

app_name = 'mensajes'

urlpatterns = [
    path('',index,name='index'),
    path('mensajes/', MensajeListView.as_view(), name='mensaje_list'),
    path('mensajes/<int:pk>/',MensajeDetailView.as_view(),name='mensaje_detail'),
    path('mensajes/usuario/',MensajeListViewByUser.as_view(), name='mensaje_by_user'),
    path('mensaje/crear',MensajeCreateView.as_view(),name='mensaje_create'),
    path('mensaje/creado/', mensajeCreated, name='mensaje_created'),
    path('mensajes/eliminar/<int:pk>/', MensajeDeleteView.as_view(), name='mensaje_delete')
]