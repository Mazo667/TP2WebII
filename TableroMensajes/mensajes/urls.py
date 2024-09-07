from django.urls import path
from .views import MensajeCreateView, MensajeDeleteView, MensajeListView, index, MensajeCreated

app_name = 'mensajes'

urlpatterns = [
    path('',index,name='index'),
    path('mensajes/', MensajeListView.as_view(), name='mensaje_list'),
    path('mensaje/crear',MensajeCreateView.as_view(),name='mensaje_create'),
    path('mensaje/creado/', MensajeCreated, name='mensaje_created'),
    path('mensajes/delete/<int:pk>/', MensajeDeleteView.as_view(), name='mensaje_delete')
]