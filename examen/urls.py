from django.contrib import admin
from django.urls import path
from simulador import views
from django.views.generic import TemplateView


urlpatterns = [
    path('preguntas/<int:subject_id>/', views.get_pregunta_by_subject, name='preguntas_by_subject'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
]



    