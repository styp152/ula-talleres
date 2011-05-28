from django.contrib import admin
from eisula.proyecto.models import ProyectoDeGrado, Persona, \
                                   PalabraClave, Materia, Biblioteca

class ProyectoDeGradoAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha_publicacion'
    fieldsets = (
        (None, {
            'fields': ('titulo', 'cota', 'resumen', 'fecha_publicacion',
                       'palabra_clave', 'enlace_repositorio', 'observacion',
                       'materia', 'biblioteca', 'nota', 'mencion_publicacion')
        }),
        ('Personas involucradas', {
            'classes': ('collapse',),
            'fields': ('autor', 'tutor', 'jurado')
        }),
    )
    list_display = ('titulo', 'cota', 'fecha_publicacion', 'autor')
    search_fields = ('autor__apellido', 'cota')
    list_filter = ('mencion_publicacion',)
    ordering = ('-fecha_publicacion',)
    list_display_links = ('autor', 'cota')

admin.site.register(Persona)
admin.site.register(PalabraClave)
admin.site.register(Materia)
admin.site.register(Biblioteca)
admin.site.register(ProyectoDeGrado, ProyectoDeGradoAdmin)
