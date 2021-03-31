from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username'])
	return HttpResponse(lista, content_type = 'application/json')



def mascota_view(request):
	if request.method == 'post':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_listar')
	else:
		form = MascotaForm()
	return render(request, 'mascota/mascota_form.html', {'form':form})



def mascota_list(request):
	mascota = Mascota.objects.all().order_by('id')
	contexto = {'mascotas':mascota}
	return render(request, 'mascota/mascota_list.html', contexto)
#def mascota_edit(request, id_mascota):
	#query sets
#	mascota = Mascota.objects.get(id=id_mascota)
#	if request.method == 'GET':
#		form = MascotaForm(intance=mascota)
#	else:
		#recoge post del formulario pero tambien instanciamos el obejto para guardar los cambios
#		form = MascotaForm(request.POST, instance=mascota)
		#validamos que el formulario sea valido
#		if form.is_valid():
			#de ser asi ,se guardan los cambios
#			form.save()
#		return redirect('mascota:mascota_listar')
#
#	return render(request, 'mascota/mascota_form.html', {'form':form})

##############################################################
					#Vistas basadas en clases#
##############################################################

#listar
class MascotaList(ListView):
	model = Mascota
	#a que template mandamos los datos
	template_name = 'mascota/mascota_list.html'
	paginate_by = 5
#crear
class MascotaCreate(CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota_listar')

class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_form.html'
	success_url = reverse_lazy('mascota_listar')

class MascotaDelete(DeleteView):
	model = Mascota
	template_name = 'mascota/mascota_delete.html'
	success_url = reverse_lazy('mascota_listar')
