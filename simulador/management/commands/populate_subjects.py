from django.core.management.base import BaseCommand
from simulador.models import Subject, Category

class Commands(BaseCommand):
    def handle(self, *args, **options):

        subjects = {
            "Matematicas": ["Algebra", "Geometria", "Trigonometria", "Calculo"],
            "Sociales": ["Historia", "Geografia", "Civica"],
            "Espanol": ["Literatura", "Ortografia", "Redaccion"],
            "Biologia": ["Zoologia", "Botanica", "Ecologia"],
            "Ingles": ["Gramática", "Vocabulario", "Comprensión"],
        }
        
        for category_name, subjects in subjects.items():
            category = Category.objects.filter(name=category_name).first()
            if not category:
                print(f"Categoria {category_name} no encontrada.")
                category = Category(name=category_name)
                category.save()

        for subjec in subjects:
            print(f"Creando asignatura: {subjec}")
            sub = Subject(
                name= subjec,
                category= category
            )
            sub.save()
        print("Asignaturas creadas exitosamente.")