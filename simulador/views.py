# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse    
from .models import Subject, Question, Respuesta, Exam


def index(request):
    return render(request, 'index.html')

def get_pregunta_by_subject(request, subject_id):
    if request.method == 'POST':
        data = request.POST
        exam = Exam.objects.create(estudiante=request.user, puntuacion=0)  # Crear un examen para el usuario
        exam.save()

        for key, value in data.items():
            if key.startswith('pregunta_'):
                question_id = key.split('_')[1]
                respuesta_dada = value
                try:
                    question = Question.objects.get(id=question_id)
                    # exam.preguntas.add(question)

                    es_correcta = (respuesta_dada == question.respuesta_correcta)
                    # Aquí podrías guardar la respuesta en la base de datos si es necesario
                    print(f"Pregunta: {question.enunciado}, Respuesta dada: {respuesta_dada}, Correcta: {es_correcta}")
                    Respuesta.objects.create(
                        question=question,
                        respuesta_dada=respuesta_dada,
                        es_correcta=es_correcta,
                        exam=exam
                    ).save()
                    
                except Question.DoesNotExist:
                    print(f"Pregunta con ID {question_id} no encontrada.")
        return redirect('index')


    subject = Subject.objects.get(id=subject_id)
    preguntas = Question.objects.filter(materia=subject)
    return render(request, 'preguntas.html', {'Question': preguntas})