from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.mascota.views import listadousuarios, mascota_view, mascota_list, \
MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete
#, mascota_edit

urlpatterns = [
#    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    #usamos .as_view(), para decirle a la clase que se trata de una vista
    url(r'^listar', login_required(MascotaList.as_view()), name='mascota_listar'),
    #Mandamos el segun parametro que es el id
    #usamos una expresion regular que reciba el parametr id_mascota para funciones
    # url(r'^editar/(?P<id_mascota>\d+)$', mascota_edit, name='mascota_editar'),
    #en clases parametro pk
     url(r'^editar/(?P<pk>\d+)$', login_required(MascotaUpdate.as_view()), name='mascota_editar'),
     url(r'^eliminar/(?P<pk>\d+)$', login_required(MascotaDelete.as_view()), name='mascota_eliminar'),
     url(r'^listado', login_required(listadousuarios), name='listado'),
]