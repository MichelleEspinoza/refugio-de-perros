import json
#from rest_framework import viewsets
#from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
#usamos un form generado por django
#importamos el que heredamos
from apps.usuario.forms import RegistroForm
#from apps.usuario.serializers import UserSerializer
#from django.shortcuts import render, redirect


class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	#como no usaremos mas el que nos daba djang importamos el que heredamos junto con este en forms.py
	#form_class = UserCreationForm
	form_class = RegistroForm
	success_url = reverse_lazy('mascota_listar')

#lass UserAPI(APIView):
#	serializer = UserSerializer
#
#	def get(self, request, formar=None):
#		lista = User.objects.all()
#		response = self.serializers(lista, many=True)
#
#		return HttpResponse(json.dumps(response.data), content_type='application/json')
