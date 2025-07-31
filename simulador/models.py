from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Subject(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Question(models.Model):
    OPCIONES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    enunciado = models.TextField()
    materia = models.ForeignKey(Subject, on_delete=models.CASCADE)
    opcion_A = models.CharField(max_length=255)
    opcion_B = models.CharField(max_length=255)
    opcion_C = models.CharField(max_length=255)
    opcion_D = models.CharField(max_length=255)
    respuesta_correcta = models.CharField(max_length=1, choices=OPCIONES)

    def __str__(self):
        return self.enunciado
    
class Exam(models.Model):
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    puntuacion = models.DecimalField(max_digits=5, decimal_places=2)
    preguntas = models.ManyToManyField(Question, through='Respuesta')

    def __str__(self):
        return f'Examen de {self.estudiante.username} - {self.fecha}'
    

class Respuesta(models.Model):
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    respuesta_dada = models.CharField(max_length=1, choices=Question.OPCIONES)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.exam} - {self.question} - {self.respuesta_dada}'