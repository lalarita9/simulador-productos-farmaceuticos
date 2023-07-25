#Desarrollo de pruebas unitarias para el modelo Laboratorio(Drilling Final, parte 5)
from django.test import TestCase 
from django.urls import reverse
from .models import Laboratorio

# Create your tests here.
class LaboratorioTests(TestCase):
    @classmethod 
    def setUpTestData(cls): 
        cls.laboratorio = Laboratorio.objects.create(nombre="Laboratorio 1", ciudad='Ciudad 1', pais='Pais 1')
    def test_model_content(self):
        self.assertEqual(self.laboratorio.nombre, "Laboratorio 1")
        self.assertEqual(self.laboratorio.ciudad, "Ciudad 1")
        self.assertEqual(self.laboratorio.pais, "Pais 1")
    def test_url_exists_at_correct_location(self): 
        response = self.client.get("/") 
        self.assertEqual(response.status_code, 200)
    def test_homepage(self): 
        response = self.client.get(reverse("mostrar-lab")) 
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, "mostrar.html") 
        self.assertContains(response, "Información de Laboratorios")
