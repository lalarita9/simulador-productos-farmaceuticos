from django.contrib import admin
#Importación de modelos(Drilling Final, parte 2)
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.

#Se agrega la clase LaboratorioAdmin, para que muestre en admin de Django: id y nombre, siendo ordenado por 
#nombre(Drilling Final, parte 2)
class LaboratorioAdmin(admin.ModelAdmin): 
    fields = ['nombre'] 
    list_display = ('id','nombre', 'ciudad', 'pais') 
    ordering = ('nombre',) 
    
#Se agrega la clase DirectorGeneralAdmin, para que muestre en admin de Django: list_display, siendo
#ordenado por nombre(Drilling Final, parte 2)
class DirectorGeneralAdmin(admin.ModelAdmin): 
    fields = ['nombre'] 
    list_display = ('id','nombre', 'laboratorio') 
    ordering = ('nombre',) 
    
#Se agrega la clase ProductoAdmin, para que muestre en admin de Django: list_display, siendo ordenado
#por nombre(Drilling Final, parte 2)    
class ProductoAdmin(admin.ModelAdmin): 
    list_display = ('id','nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta') 
    ordering = ('nombre',) 
    list_filter = ('nombre', 'laboratorio')

admin.site.register(Laboratorio, LaboratorioAdmin) 
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)

