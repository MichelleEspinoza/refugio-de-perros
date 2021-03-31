from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm
from django.urls import reverse_lazy

def index_adopcion(request):
	return HttpResponse("Index2")

class SolicitudList(ListView):
	model = Solicitud
	template_name = 'adopcion/solicitud_list.html'
	paginate_by = 5

class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('solicitud_listar')
	
	#sobreescribimos la funcion
	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		#si form no esta en el contexto 
		if 'form' not in context:
			#lo agregamos
			context['form'] = self.form_class(self.request.GET)
		#ahora agreegamos el segundo formulario a nuestro contexto
		#si no tenemos en dos lo agregamos
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		#retonarmos el contexto. CON ESTO SOLO TENEMOS PINTADOS LOS FORMS EN HTML
		return context


#Ahora guardaremos los valores y crearemos la relacion de esos html		
	#primero recibimos todos los datos
	def post(self, request, *args, **kwargs):
		#accedemos al objeto
		self.object = self.get_object
		#recogemos de los dos formularios la informacion de los forms.
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		#ahora evaluamos si son validos los valores para guardarlos
		if form.is_valid() and form2.is_valid():
		#si si generamos una variable para recoger los datos pero aun no los guarda
		#por qe espera a los valores del segundo form
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			#ahora retornamos
			return HttpResponseRedirect(self.get_success_url())
		#si no es valido devolvemos el contexto.
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))


class SolicitudUpdate(UpdateView):
	#llamamos los dos modelos
	model = Solicitud
	second_model = Persona
	template_name = 'adopcion/solicitud_form.html'
	form_class = SolicitudForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('solicitud_listar')


	def get_context_data(self, **kwargs):
	    context = super(SolicitudUpdate, self).get_context_data(**kwargs)
	    #pk variable
	    pk = self.kwargs.get('pk', 0)
	    #la el objeto que sea igual al pk
	    solicitud = self.model.objects.get(id=pk)
	    #lo mismo pero que me de el id sea igual al objeto de solicitud e igual al atributo de la persona
	    persona = self.second_model.objects.get(id=solicitud.persona_id)
	    #validar que los forms esten en el contexto. (pintamos)
	    if 'form' not in context:
	    	context['form'] = self.form_class()
	    if 'form2' not in context:
	    	context['form2'] = self.second_form_class(instance=persona)
	    context['id'] = pk
	    return context
#sobreescibimos(obtenemos)
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_solicitud = kwargs['pk']
		solicitud = self.model.objects.get(id=id_solicitud)
		persona = self.second_model.objects.get(id=solicitud.persona_id)
		form = self.form_class(request.POST, instance=solicitud)
		form2 = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())


class SolicitudDelete(DeleteView):
	model = Solicitud
	template_name = 'adopcion/solicitud_delete.html'
	success_url = reverse_lazy('solicitud_listar')			