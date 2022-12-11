from django.db import models

# Create your models here.
class CrearProyecto(models.Model):
    foto =  models.CharField(max_length=200)
    titulo_del_proyecto = models.CharField(max_length=200)
    descripción_del_proyecto = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    url_de_github = models.CharField(max_length=200)

    class Meta:
        db_table = "proyectos"