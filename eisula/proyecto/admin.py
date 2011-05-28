from django.contrib import admin
from eisula.proyecto.models import ProyectoDeGrado, Persona, \
                                   PalabraClave, Materia, Biblioteca

admin.site.register(Persona)
admin.site.register(PalabraClave)
admin.site.register(Materia)
admin.site.register(Biblioteca)
admin.site.register(ProyectoDeGrado)
