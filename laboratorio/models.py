from django.db import models
#Se importa datetime(Drilling Final, parte 1)
import datetime

# Register your models here.
years_choices = [] 
for annio in range(2000, (datetime.datetime.now().year+1)): 
    years_choices.append((annio,annio))

#Se crea la clase Laboratorio(Drilling Final, parte 1)
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=200)
    #Se crea los modelos(Drilling Final, parte 4)
    pais= models.CharField(max_length=200)
    ciudad= models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre

#Se crea la clase DirectorGeneral(Drilling Final, parte 1)
class DirectorGeneral(models.Model): 
    #Se define un modelo de tipo cascada, con una relación de uno a uno
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=250)
    especialidad= models.CharField(max_length=250)

    def __str__(self): 
        return self.nombre

#Se crea la clase Producto(Drilling Final, parte 1)
class Producto(models.Model):
    nombre = models.CharField(max_length=250)
    #Se define un modelo de tipo cascada, nos indica a que laboratorio pertenece relacionándolo con una
    #llave foránea al módelo Laboratorio
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.IntegerField(choices=years_choices, default=2015) 
    p_costo = models.DecimalField(null=False, decimal_places=2, max_digits=10, default=0 ) 
    p_venta = models.DecimalField(null=False, decimal_places=2, max_digits=10, default=0)
    
    def __str__(self):
        return self.nombre
