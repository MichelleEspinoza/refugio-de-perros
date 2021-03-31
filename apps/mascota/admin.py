from django.contrib import admin

from apps.mascota.models import Vacuna, Mascota

admin.site.register(Vacuna)
admin.site.register(Mascota)