from django.conf.urls import url, include
from apps.productos.views import index, producto_view, ProductoList, producto_edit, producto_delete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(producto_view), name='producto_view'),
    url(r'^listar', ProductoList.as_view(), name='producto_listar'),
    url(r'^editar/(?P<id_producto>\d+)/$', login_required(producto_edit), name='producto_editar'),
    url(r'^eliminar/(?P<id_producto>\d+)/$', login_required(producto_delete), name='producto_delete'),
]
