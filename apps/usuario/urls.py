from django.conf.urls import url
from apps.usuario.views import RegistroUsuario
# UserAPI
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^registrar$',RegistroUsuario.as_view(), name='registrar'),
   # url(r'^api$', login_required(UserAPI.as_view()), name='api'),
    #url(r'^eliminar/(?P<pk>\d+)$', MascotaDelete.as_view(), name='mascota_eliminar'),
]