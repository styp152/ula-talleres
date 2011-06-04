from django.views.generic import ListView, DetailView

from eisula.proyecto.models import ProyectoDeGrado, Estudiante, Profesor, \
                                   Materia, Biblioteca

class IndexView(ListView):
    queryset = ProyectoDeGrado.objects.order_by("-fecha_publicacion")
    context_object_name="project_list"
    #template_name="proyecto/proyectodegrado_list.html"


class AuthorView(ListView):
    model = Estudiante # shorthand: ProyectoDeGrado.objects.all()
    context_object_name="author_list"
    #template_name="proyecto/estudiante_list.html"


class AuthorDetailView(DetailView):
    model = Estudiante
    context_object_name="author"

    def get_context_data(self, **kwargs):
        # Llamado a la implementacion base para obtener el contexto
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # Agregando una consulta para obtener el proyecto de grado.
        #context['project'] = ProyectoDeGrado.objects(autor=
        return context


class ProfessorView(ListView):
    model = Profesor
    context_object_name="professor_list"
    #template_name="proyecto/profesor_list.html"


class CourseView(ListView):
    model = Materia
    context_object_name="course_list"
    #template_name="proyecto/materia_list.html"


class LibraryView(ListView):
    model = Biblioteca
    context_object_name="library_list"
    #template_name="proyecto/biblioteca_list.html"
