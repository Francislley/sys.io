from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^perfil_list/', perfil_list, name='perfil_list'),
    url(r'^perfil_new/', perfil_new, name='perfil_new'),
    url(r'^perfil_edit/(?P<pk>[0-9]+)', perfil_edit, name='perfil_edit'),
    url(r'^perfil_remove/(?P<pk>[0-9]+)', perfil_remove, name='perfil_remove')

]
