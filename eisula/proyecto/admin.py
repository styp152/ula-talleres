from django.contrib import admin
from eisula.proyecto.models import (ProyectoDeGrado, Estudiante, Profesor,
                                    PalabraClave, Materia, Biblioteca)

class ProyectoDeGradoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha_publicacion'
    fieldsets = (
        (None, {
            'fields': ('titulo', 'autor', 'tutor', 'jurado', 'cota', 'resumen',
                       'fecha_publicacion', 'palabra_clave',
                       'enlace_repositorio',
                       'biblioteca','mencion_publicacion')
        }),
        ('Campos opcionales', {
            'classes': ('collapse',),
            'fields': ('nota', 'observacion', 'materia')
        }),
    )
    list_display = ('titulo', 'cota', 'fecha_publicacion', 'autor')
    search_fields = ('autor__apellido', 'titulo', 'cota')
    list_filter = ('mencion_publicacion',)
    ordering = ('-fecha_publicacion',)
    list_display_links = ('autor', 'cota')

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(PalabraClave)
admin.site.register(Materia)
admin.site.register(Biblioteca)
admin.site.register(ProyectoDeGrado, ProyectoDeGradoAdmin)
