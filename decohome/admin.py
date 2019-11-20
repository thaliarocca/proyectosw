from django.contrib import admin
from .models import Cita
from .models import Producto
from .models import Administrador
from .models import Cliente

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    pass
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass
@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    pass