from django.conf.urls.defaults import patterns, url
from eisula.proyecto.views import IndexView, CourseView, CourseDetailView, \
                                  ProfessorView, ProfessorDetailView, \
                                  AuthorView, AuthorDetailView, \
                                  LibraryView, LibraryDetailView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^materias/(?P<pk>\d+)/$', CourseDetailView.as_view()),
    url(r'^materias/$', CourseView.as_view()),
    url(r'^profesores/(?P<pk>\d+)/$', ProfessorDetailView.as_view()),
    url(r'^profesores/$', ProfessorView.as_view()),
    url(r'^autores/(?P<pk>\d+)/$', AuthorDetailView.as_view()),
    url(r'^autores/$', AuthorView.as_view()),
    url(r'^bibliotecas/(?P<pk>\d+)/$', LibraryDetailView.as_view()),
    url(r'^bibliotecas/$', LibraryView.as_view()),
)
