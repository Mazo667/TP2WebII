from django.db import models

class Mensaje(models.Model):
    remitente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    texto = models.TextField()
    fecha_hora = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.remitente} a {self.destinatario}: {self.texto}"