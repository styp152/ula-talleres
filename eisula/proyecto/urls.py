from django.conf.urls.defaults import patterns, url
from eisula.proyecto.views import IndexView, CourseView, ProfessorView, \
                                  AuthorView, AuthorDetailView, LibraryView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^materias/$', CourseView.as_view()),
    url(r'^profesores/$', ProfessorView.as_view()),
    url(r'^autores/(?P<pk>\d+)/$', AuthorDetailView.as_view()),
    url(r'^autores/$', AuthorView.as_view()),
    url(r'^bibliotecas/$', LibraryView.as_view()),
)
