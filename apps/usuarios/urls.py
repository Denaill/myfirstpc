from django.conf.urls import url
from apps.usuarios.views import RegistroUsuario, UsuarioList, usuario_edit, usuario_delete
from django.contrib.auth.decorators import login_required

urlpatterns = [
   url(r'^registrar', RegistroUsuario.as_view(), name="registrar"),
   url(r'^listar$', login_required(UsuarioList.as_view()), name="usuario_listar" ),
   url(r'^editar/(?P<id_usuario>\d+)/$', login_required(usuario_edit), name='usuario_editar'),
   url(r'^eliminar/(?P<id_usuario>\d+)/$', login_required(usuario_delete), name='usuario_delete')
]
