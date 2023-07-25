from django.urls import path
from . import views
#creación de urls (Drilling Final, parte 4)
urlpatterns = [
    path('', views.insertar_lab, name='insertar-lab'),
    path('mostrar/', views.mostrar_lab, name='mostrar-lab'),
    path('editar/<int:pk>', views.editar_lab, name='editar-lab'),
    path('actualizarlab/<int:id>', views.actualizar_lab, name='actualizar-lab'),
    path('eliminar/<int:pk>', views.eliminar_lab, name='eliminar-lab'),
    path('pythonShell/', views.python_shell, name='python-shell'),
        
]