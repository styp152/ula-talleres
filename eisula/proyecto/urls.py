from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView
from eisula.proyecto.models import ProyectoDeGrado

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
        model=ProyectoDeGrado,
        context_object_name="proyectos",
    )),
)
