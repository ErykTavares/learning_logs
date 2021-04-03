from django.conf.urls import url
from django.urls.conf import path, re_path
from . import views

"""Define os padroes de urls"""

urlpatterns = [
    #pagina inicial
    path(r"", views.index, name="index"),
    #pagina todos os  assuntos
    re_path(r"topics/", views.topics, name="topics"),
    #pagina de um assunto em especifico
    re_path(r"topic/(?P<topic_id>\d+)/", views.topic, name="topic"),
    #pagina para criação de um novo assunto
    re_path(r"new_topic/", views.new_topic, name="new_topic"),
    #pagina para adicionar uma nova entrada
    re_path(r"new_entry/(?P<topic_id>\d+)/", views.new_entry, name="new_entry"),
    re_path(r"edit_entry/(?P<entry_id>\d+)/", views.edit_entry, name="edit_entry"),
]



