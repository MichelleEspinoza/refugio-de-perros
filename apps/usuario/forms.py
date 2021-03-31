from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#esta clase hereda de UserCreationForm, osea que tiene los datos de esa clase en el Meta agreamos los adicionales que deseamos.
class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}
		