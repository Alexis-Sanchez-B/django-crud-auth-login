#from django import ModelForm
from .models import Task
from django import forms

#Crea Formulario en base a la clase Task creada en la BD solo con los datos necesarios
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Write a Title'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Write a Description'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }
