""" PART 6 : FORMULARIO REGISTRO """

# PART 6 importamos lso modulos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms



# PART 6 - Informacion quiero recopilar 
class FormRegistro(UserCreationForm):
    nombre = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre*'}) )
    correo = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))

    # PART 6 - Informacion completa del formulario del registro
    class Meta:
        model = User
         # PART 6 - Ai apareceran en el formulario
        fields = ('nombre', 'username', 'correo', 'password1', 'password2') 


    # PART 6 -  llama al constructor de la clase padre (FormularioRegistro) para asegurar que  el formulario se inicializa correctamente 
    def __init__(self, *args, **kwargs):
        super(FormRegistro, self).__init__(*args, **kwargs)

        # PART 6 - Personalizacion de los campos del fomulario
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'nombre usuario'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small> Sólo letras, dígitos y @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña*'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Tu contraseña no puede corta ni cumun.</li><li>Su contraseña debe contener al menos 8 caracteres.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña*'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Introduzca la misma contraseña que antes, para la verificación</small></span>'	
