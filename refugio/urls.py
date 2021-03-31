
from django.conf.urls import url, include
from django.contrib import admin
#por defecto de django
#from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mascota/', include('apps.mascota.urls')),
    url(r'^adopcion/', include('apps.adopcion.urls')),
    url(r'^usuario/', include('apps.usuario.urls')),
    #login defecto django
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name= 'index.html'), name='login'),
    url('', auth_views.LoginView.as_view(template_name= 'index.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    url(r'^reset/password_reset/$', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset_form.html', email_template_name = 'registration/password_reset_email.html'), name = 'password_reset'),
    url(r'^password_reset_done/$', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'), name = 'password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'), name='password_reset_complete'),
] 
