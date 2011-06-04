from django.conf.urls.defaults import patterns, url
from eisula.proyecto.views import IndexView, CourseView, ProfessorView, \
                                  AuthorView, LibraryView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^materia/$', CourseView.as_view()),
    url(r'^profesor/$', ProfessorView.as_view()),
    url(r'^autor/$', AuthorView.as_view()),
    url(r'^biblioteca/$', LibraryView.as_view()),
)
