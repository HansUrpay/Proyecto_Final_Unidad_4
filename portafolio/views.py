from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View, FormView
from .forms import CrearProyectoForm
from .models import CrearProyecto

# Create your views here.

# # Create your views here.
# class Inicio(View):
#     def get(self, request):
#         proyectos = CrearProyecto.objects.all()
#         context = {"proyectos": proyectos}
#         return render(request, "index.html", context)

class Inicio(View):
    def get(self, request):
        return render(request, "portafolio/index.html")

class CreateProject(FormView):
    model = CrearProyecto
    form_class = CrearProyectoForm
    template_name = "portafolio/crear_proyecto.html"

    def form_valid(self, form):
        CrearProyecto.objects.create(**form.cleaned_data)
        return redirect("index")