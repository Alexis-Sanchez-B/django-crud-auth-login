from django.forms import ModelForm
from .models import Task

#Crea Formulario en base a la clase Task creada en la BD solo con los datos necesarios
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']
