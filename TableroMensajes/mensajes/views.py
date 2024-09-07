from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensaje
from .forms import MensajeForm

def index(request):
    return render(request,'mensajes/index.html')

def mensajeCreated(request):
    return render(request,'mensajes/mensaje_created.html')

class MensajeListView(View):
    def get(self, request):
        usuario = request.GET.get('usuario', None)
        
        if usuario:
            # Filtrar mensajes por remitente o destinatario
            mensajes = Mensaje.objects.filter(remitente__icontains=usuario) | Mensaje.objects.filter(destinatario__icontains=usuario)
        else:
            mensajes = Mensaje.objects.all()  # Si no hay usuario, mostrar todos los mensajes

        return render(request, 'mensajes/mensaje_list.html', {'mensajes': mensajes})

class MensajeDetailView(View):
    def get(self,request,pk):
        mensaje = get_object_or_404(Mensaje, pk=pk)
        return render(request,'mensajes/mensaje_detail.html',{'mensaje':mensaje})

class MensajeCreateView(View):
    def get(self, request):
        form = MensajeForm()
        return render(request, 'mensajes/mensaje_create.html', {'form': form})

    def post(self, request):
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajes:mensaje_created')  
        return render(request, 'mensajes/index.html', {'form': form})

class MensajeDeleteView(View):
    def post(self, request, pk):
        mensaje = get_object_or_404(Mensaje, pk=pk)
        mensaje.delete() 
        return redirect('mensajes:mensaje_list') 