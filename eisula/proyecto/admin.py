from django.contrib import admin
from eisula.proyecto.models import Persona, PalabraClave, Materia, \
                                   Biblioteca, ProyectoDeGrado

admin.site.register(Persona)
admin.site.register(PalabraClave)
admin.site.register(Materia)
admin.site.register(Biblioteca)
admin.site.register(ProyectoDeGrado)

