from django.shortcuts import render, redirect 
from .models import Laboratorio
from django.contrib import messages
#Creación de vistas (Drilling Final, parte 4)
# Crea método insertar_lab
def insertar_lab(request): 
    if request.method == "POST": 
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad'] 
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais= pais)
        laboratorio.save()
        messages.success(request, 'El Laboratorio fue agregado correctamente')
        return redirect('mostrar/') 
    else: 
        return render(request, 'insertar.html')
#Crea el método mostrar_lab
def mostrar_lab(request): 
    laboratorio = Laboratorio.objects.all() 
    num_visitas = request.session.get('num_visitas', 0) 
    request.session['num_visitas'] = num_visitas + 1 
    context = {
        'laboratorios': laboratorio,
        'num_visitas': num_visitas
    }
    return render(request,'mostrar.html', context)
    
# Se crea método editar_lab
def editar_lab(request, pk): 
    laboratorio = Laboratorio.objects.get(id=pk) 
    context = {
        'laboratorio': laboratorio
    }
    return render(request,'editar.html', context) 

# Crea el método actualizarlab
def actualizar_lab(request, id): 
    nombre_lab = request.POST['nombre'] 
    ciudad_lab = request.POST['ciudad'] 
    pais_lab = request.POST['pais'] 
    laboratorio = Laboratorio.objects.get(id=id) 
    laboratorio.nombre = nombre_lab
    laboratorio.ciudad = ciudad_lab
    laboratorio.pais = pais_lab
    laboratorio.save() 
    messages.success(request, 'El Laboratorio fue actualizado exitoxamente')
    return redirect('mostrar-lab')

# Crea el método eliminar_lab
def eliminar_lab(request, pk): 
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == 'POST': 
        laboratorio.delete() 
        messages.success(request, 'El Laboratorio fue eliminado exitoxamente')
        return redirect('mostrar-lab') 
    context = {
        'laboratorio': laboratorio
    }
    return render(request, 'eliminar.html', context)
# Crea el método python_shell
def python_shell(request):
    
    return render(request, "pythonShell.html")
