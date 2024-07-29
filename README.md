# BussConecta

- PART 0 - Instalacion de la aplicaion
- PART 1 - MySQL configurafion 
- PART 2 - Git & Github
- PART 3 - Build Basic App
- PART 4 - Log In
- PART 5 - Log Out
- PART 6 - Register User
- PART 7 - Database Model
- PART 8 - 
- PART 9 - 


Despues de acabar con la parte basica que es mas en front end ahora hay que empezar hacer la web mas dinamica 

Craando la logica que funcionara para que se pueda realizar en el siguiente orden :

- Iniciar Session

- Cerrar Session

- Poder registrarse 

- Modelo de la base se datos (Tipo de Informacion que vamos a guardar en la bbdd )

- Vista Modelo BBDD ( poder ver la informacion guardada en la base de datos )

    - De forma General 
    - De forma Individual

- Tecnologias que vamos a utilizar 
    - django 



##### GIT & GITHUB 

Registrar y subir la aplicacion a github 

##### BUILD APP BASIC 

Contruimos todo lo basico de apliacion desde la urls asta  
todo la pagian estatica de pricipal antes de inicio de seccion


##### LOG IN ( USER )

Ahora vamos a contruir el log ig 
- importamos log in , log out y autenticacion desde django



##### REGISTER 

La función que has compartido parece ser parte de una clase que define un formulario en Django, un popular framework web de Python. La función `__init__` es el método constructor de la clase, que se utiliza para inicializar instancias de dicha clase. Aquí se está personalizando el comportamiento de un formulario, probablemente de registro de usuarios (SignUpForm). Vamos a desglosar lo que hace esta función:

```python
def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
    self.fields['username'].label = ''
    self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password1'].label = ''
```

### Detalles del código:

1. **`def __init__(self, *args, **kwargs):`**:
   - Esta es la definición del método constructor de la clase. `self` se refiere a la instancia de la clase, `*args` permite recibir un número variable de argumentos posicionales, y `**kwargs` permite recibir un número variable de argumentos con nombre.

2. **`super(SignUpForm, self).__init__(*args, **kwargs)`**:
   - Esta línea llama al constructor de la clase padre (en este caso, la clase base de formularios de Django) para asegurarse de que el formulario se inicializa correctamente con los argumentos proporcionados.

3. **Personalización de los campos del formulario**:
   - `self.fields['username']`: Accede al campo del formulario llamado `username`.
     - `widget.attrs['class'] = 'form-control'`: Agrega la clase CSS `form-control` al widget del campo, que suele ser utilizado por Bootstrap para aplicar estilos específicos.
     - `widget.attrs['placeholder'] = 'User Name'`: Establece un texto de marcador de posición para el campo, que se muestra cuando el campo está vacío.
     - `label = ''`: Elimina la etiqueta del campo (esto es útil si se desea manejar las etiquetas manualmente en el HTML).
     - `help_text`: Agrega un texto de ayuda debajo del campo, proporcionando información adicional al usuario.

   - `self.fields['password1']`: Accede al campo del formulario llamado `password1` (probablemente el campo de contraseña).
     - `widget.attrs['class'] = 'form-control'`: Agrega la clase CSS `form-control` al widget del campo.
     - `widget.attrs['placeholder'] = 'Password'`: Establece un texto de marcador de posición para el campo.
     - `label = ''`: Elimina la etiqueta del campo.

### Propósito del código:
Este método constructor está personalizado para modificar el aspecto y comportamiento de los campos del formulario `SignUpForm`. En concreto, se están ajustando los atributos del widget de los campos `username` y `password1` para mejorar la apariencia y usabilidad del formulario, utilizando clases de CSS (como las de Bootstrap) y proporcionando texto de ayuda al usuario.

### Ejemplo de uso en un formulario de Django:
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
```

En este ejemplo, `SignUpForm` extiende `UserCreationForm`, y el constructor personalizado ajusta los campos del formulario para que tengan un estilo específico y mejoren la experiencia del usuario.

