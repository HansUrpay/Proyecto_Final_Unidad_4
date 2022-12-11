from django.urls import path
from .views import Inicio, CreateProject

urlpatterns = [
    path("", Inicio.as_view(), name="inicio"),
    path("crear/", CreateProject.as_view(), name="crear"),
]