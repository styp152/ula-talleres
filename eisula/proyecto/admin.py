from django.contrib import admin
from eisula.proyecto.models import ProyectoDeGrado, Tutor, Autor, \
                                   PalabraClave, Materia, Biblioteca

admin.site.register(ProyectoDeGrado)
admin.site.register(Tutor)
admin.site.register(Autor)
admin.site.register(PalabraClave)
admin.site.register(Materia)
admin.site.register(Biblioteca)
