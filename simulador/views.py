# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse    
from .models import Subject, Question

def index(request):
    return render(request, 'index.html')

def get_pregunta_by_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    preguntas = Question.objects.filter(materia=subject)
    return render(request, 'preguntas.html', {'Question': preguntas})