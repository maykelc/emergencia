from django.contrib import admin
from .models import Alerta, Usuario, ubicacion

# Register your models here.
admin.site.register(Alerta)
admin.site.register(Usuario)
admin.site.register(ubicacion)