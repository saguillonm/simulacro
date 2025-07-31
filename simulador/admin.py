from django.contrib import admin
from .models import Category, Subject, Question, Exam, Respuesta
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')
    search_fields = ('nombre',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('enunciado', 'materia', 'respuesta_correcta')
    search_fields = ('enunciado',)
    list_filter = ('materia', 'respuesta_correcta')

class ExamAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'fecha', 'puntuacion')
    search_fields = ('estudiante__username',)


class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('exam', 'question', 'respuesta_dada', 'es_correcta')
    search_fields = ('exam__estudiante__username', 'question__enunciado')



#Registra con la clase personalizada
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Respuesta, RespuestaAdmin)

