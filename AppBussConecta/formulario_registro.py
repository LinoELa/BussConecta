""" PART 6 : FORMULARIO REGISTRO """

# PART 6 importamos lso modulos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from .models import historial




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






# ------------------ 
# PART 13.10 Crear formulario

#  PART 13.11 usar  ModelForm
class FormAgregar(forms.ModelForm):

    # 13.12 Como quiero que aparezcan 

    inicio = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Inicio", "class":"form-control"}), label="")

    final = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Final", "class":"form-control"}), label="")

# ------------------ Para hacer que no sea obligatario y que pueda pasar  el argumento vacio como un None

    poste_1 = forms.CharField(required=True, widget=forms.NumberInput(attrs={"placeholder":"Numero Poste ", "class":"form-control"}), label="")

    poste_2 = forms.CharField(required=False, widget=forms.NumberInput(attrs={"placeholder":"Numero Poste ", "class":"form-control"}), label="")

    poste_3 = forms.CharField(required=False, widget=forms.NumberInput(attrs={"placeholder":"Numero Poste ", "class":"form-control"}), label="")

    notas = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"Notas", "class":"form-control"}), label="")


    #  13.13 Asignar la clase Meta y decir que modelo queremos usar 

    class Meta:
        model = historial
        # la (,) al final es importante
        exclude = ('user',)


    #  CLASE PARA QUE PASE UN None en ves de VACIO -----------
    # Poste 2 
    def limpiar_poste_2(self):
        datos = self.cleaned_data('poste_2')
        if datos == '':
            return None
        return datos
    
    # Poste 3 
    def limpiar_poste_3(self):
        datos = self.cleaned_data('poste_3')
        
        if datos == '':
            return None
        
        return datos


    # 13.14 Importamos el modelo que acabamos de clear a view.py




    """
    El error Field 'poste_2' expected a number but got '' ocurre porque Django espera un 
    número en el campo poste_2, pero recibe una cadena vacía (''). Esto sucede porque aunque poste_2 está definido como
    blank=True y null=True, el formulario de Django está enviando una cadena vacía en lugar de None.
    """