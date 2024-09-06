from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensaje
from .forms import MensajeForm

class MensajeView(View):
    def get(self, request):
        mensajes = Mensaje.objects.all()
        form = MensajeForm()
        return render(request, 'mensajes/mensaje_list.html', {'mensajes': mensajes, 'form': form})

    def post(self, request):
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('mensaje_list') 
        mensajes = Mensaje.objects.all() 
        return render(request, 'mensajes/mensaje_list.html', {'mensajes': mensajes, 'form': form})

class MensajeDeleteView(View):
    def post(self, request, pk):
        mensaje = get_object_or_404(Mensaje, pk=pk)
        mensaje.delete() 
        return redirect('mensaje_list') 