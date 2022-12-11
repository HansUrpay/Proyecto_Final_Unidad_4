from django import forms

class CrearProyectoForm(forms.Form):
    foto =  forms.CharField(max_length=200)
    titulo_del_proyecto = forms.CharField(max_length=200)
    descripción_del_proyecto = forms.CharField(max_length=200)
    tags = forms.CharField(max_length=200)
    url_de_github = forms.CharField(max_length=200)