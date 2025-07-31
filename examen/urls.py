from django.contrib import admin
from django.urls import path
from simulador import views
from django.views.generic import TemplateView


urlpatterns = [
    path('pregunta_lectura', TemplateView.as_view(template_name='pregunta_lectura.html'), name='pregunta_lectura'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
]



    