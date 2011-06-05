from django.views.generic import (ListView, DetailView, ArchiveIndexView,
                                  YearArchiveView, MonthArchiveView,
                                  DayArchiveView, DateDetailView)

from eisula.proyecto.models import (ProyectoDeGrado, Estudiante, Profesor,
                                    Materia, Biblioteca)

class ThesisArchiveIndexView(ArchiveIndexView):
    model = ProyectoDeGrado
    date_field = "fecha_publicacion"
    context_object_name = "project_latest"
    #template_name = "proyecto/proyectodegrado_archive.html"


class ThesisYearArchiveView(YearArchiveView):
    model = ProyectoDeGrado
    date_field = "fecha_publicacion"


class ThesisMonthArchiveView(MonthArchiveView):
    model = ProyectoDeGrado
    date_field = "fecha_publicacion"


class ThesisDayArchiveView(DayArchiveView):
    model = ProyectoDeGrado
    date_field = "fecha_publicacion"


class ThesisDateDetailView(DateDetailView):
    model = ProyectoDeGrado
    date_field = "fecha_publicacion"


class AuthorView(ListView):
    model = Estudiante # shorthand: ProyectoDeGrado.objects.all()
    context_object_name = "author_list"
    #template_name = "proyecto/estudiante_list.html"


class AuthorDetailView(DetailView):
    model = Estudiante # = Estudiante.objects.filter(id=pk)
    context_object_name = "author"
    #template_name = "proyecto/estudiante_detail.html"

    def get_context_data(self, **kwargs):
        # Llamado a la implementacion base para obtener el contexto
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        # Agregando una consulta para obtener el proyecto de grado.
        context['project'] = ProyectoDeGrado.objects.get(autor=self.object)
        return context


class ProfessorView(ListView):
    model = Profesor
    context_object_name = "professor_list"
    #template_name = "proyecto/profesor_list.html"


class ProfessorDetailView(DetailView):
    model = Profesor
    context_object_name = "professor"
    #template_name = "proyecto/profesor_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProfessorDetailView, self).get_context_data(**kwargs)
        context['projects'] = ProyectoDeGrado.objects.filter(tutor=self.object)
        return context


class CourseView(ListView):
    model = Materia
    context_object_name = "course_list"
    #template_name = "proyecto/materia_list.html"


class CourseDetailView(DetailView):
    model = Materia
    context_object_name = "course"


class LibraryView(ListView):
    model = Biblioteca
    context_object_name = "library_list"
    #template_name = "proyecto/biblioteca_list.html"


class LibraryDetailView(DetailView):
    model = Biblioteca
    context_object_name = "library"
