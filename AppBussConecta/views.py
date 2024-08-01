from django.shortcuts import render

from django.shortcuts import redirect

# # PARTE 4 - 5(LOGOUT)
from django.contrib.auth import authenticate , login , logout

# PARTE 4 - importamos mensajes para cuando alqguien inicia sesion
from django.contrib import messages 

# PARTE 6 - Importar el formualario de registro
from .formulario_registro import FormRegistro

# PART 8.02
from .models import historial


# PART 13.14 
from .formulario_registro import FormAgregar





# Create your views here.

# --------------------------------- INICIO - PAGINA DE INICIO ----------------------------------------------#

def inicio(request):
    #para los usuario que no estan registrados
    return render(request, 'inicio.html', {})

# --------------------------------- HOME  ----------------------------------------------#

def home(request):
    # PART 8.01 - Queremos que aparezca solo cuando se ha iniciado session
    # PART 8.03 - Coge todo de la tabla de modelos  y lo asigna a la variable histora_record
    historia_records = historial.objects.all()

    # PART 8.03 - le ppasamos historia_records para que : que se pueda ver  ver historial en pantalla 
    # PART 8.03 - y cuando no postea nada pueda ver el historial( ahora variable : historia_record) tambien
    #Part 3 : 
    return render(request, 'home.html' , {'historia_records':historia_records})



# --------------------------------- INICIAR SESION ----------------------------------------------#


# PARTE 4 - Nuesta funcion no se peude llamar login o logout porque son palabras
def iniciar_sesion(request):
    # PART 4 - Check si el usuario esta logueado, Metodo 'POST' del formulario

    # PART 4 : Vamos a coger todo lo que they submit  on the form usando request y 'POST'

    # PART 4 - Metodo POST y la condicion es para los usuaro que quieren postear algo por eso 'POST'
    if request.method == 'POST':
        # PART 4 username - password porque son los nosmbres que le hemos asigando al formulario en Iniciar sesion
        username = request.POST['username']
        password = request.POST['password']

        # PART 4 : AUTENTIFICACION- logica para decir si es un correcto el username y el password pues que haga un login
        user = authenticate(request, username=username, password=password)

        # PART4 : VERIFICAR - para verificar si es valido el usuario y que va a iniciar session
        if user is not None:
            login(request, user)
            messages.success(request, 'Enhorabuena, has iniciado sesión!')

            #PART 4 que le rediceccione a home 
            return redirect('home')
        #PART 4 - mensaje de error si es incorecto
        else:
            messages.error(request, 'Error al iniciar session. Porfavor intentalo de nuevo')
            # PART 4 - NO USO EL REDIRECT porque data un error 
            # return redirect(request, 'iniciar_sesion.html')

    # PART 4 - no pongo 'ELSE' - para eviarar el error de 
    # ERROR : ValueError at /iniciar_sesion / 
    # ERROR : The view AppBussConecta.views.iniciar_sesion didn't return an HttpResponse object. It returned None instead.

    return render(request, 'iniciar_sesion.html', {})

# ---------------------------------  PART 5 CERRAR SESION ----------------------------------------------#

# PARTE 5 - 
def cerrar_sesion(request):
    # PART 5 - es facil , solo hay que llamar a la funcion de logout
    logout(request)

    # PART 5 - Mensaje de logout
    messages.success(request, 'Has cerrado session')

    # PART 5 - Redigir a la pagina rincipal 
    return redirect ('inicio')


# ---------------------------------  PART 6 REGISTRO USUARIOS ----------------------------------------------#

# ' Hay muchos nombres resevados para los formulario y autentificiacion ' 


# PART 6 
def registro_user(request):

    # PART 6.04 - Despues de crear el formulario de registro 

    # PART 6.04 - 1 Si rellenan el post  de la funcion registro_user envialo a nuestro formulario y haz algo
    if request.method == 'POST':

        # PART 6.05 Haz algo 
        formulario = FormRegistro(request.POST)

        #PART 6.06 Que queremos hacer, - Verificar si es valido el formulario y despues guardarlo
        if formulario.is_valid():
            formulario.save()
           
            # PART 6.07 - Conger la informacion del fomulario para  Autentificacion 
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']

            # PART 6.08 - AUTENTIFICACION- logica para decir si es un correcto el username y el password 
            user = authenticate(username=username,password=password )

            # PART 6.09 - LOGIN - En caso autentificarse con éxito: 
            login(request, user)

            messages.success(request, 'Registro con exito!')

            return redirect('home')
    # PART 6.04 - 2 : Cuando no rellenana o  no han rellenado el formulario  
    else:
        formulario = FormRegistro()
        return render(request, 'registro.html', {'formulario':formulario})
        

    return render(request, 'registro.html', {'formulario':formulario})




# --------------------------------  PART 10 MODELOS INDIVIDUALES : VISTA ----------------------------------------------#

# PART 10.02 - pk :; que aparece en la url ().../ubicacion/1)
def historial_ubicacion(request, pk):
    # PART 10.03 Revisar si  estas logeado  o NO
    if request.user.is_authenticated:
        #PART 10.4 Revisar las ubicaciones 
        # PART 10.04 "GET" - id = Es el id automatico de las migraciones (id que queremos coger)
        ubicacion_historial = historial.objects.get(id=pk)
        # PART 10.06 - historial de ubicaciones 
        return render(request, 'ubicacion.html', {'ubicacion_historial':ubicacion_historial})
    # PART 10.07 - En caso que no este autentificado
    else:
        messages.error(request,  'Tienes que iniciar session')
        return redirect('inicio')


# PART 10.08 ir a la plantilla ubicacion.html






# --------------------------------  PART 12 BORRAR UBICACION ----------------------------------------------#


# PART 12.01

def borrar_ubi_historial(request, pk):

    # PART 12.03 Revisar si  estas logeado  o NO
    if request.user.is_authenticated:

        # part 12.02 Borrar funcion
        delete_it = historial.objects.get(id=pk)
        delete_it.delete()

        # Part 12.03
        messages.success(request, 'Registro eliminado!')
        return redirect('home')
    else:
        messages.error(request, 'Debe iniciar sesión p')
        return redirect('inicio')
    
# PART 12.04 id a ubicacion.html para poner el link 


# --------------------------------  PART 13 AGREGAR UBICACION ----------------------------------------------#

# PART 13.01
def agregar_ubi_historial(request):

    # PART 13.15 
    formulario_agragar = FormAgregar(request.POST or None)
    # PART 13.16 
    if request.user.is_authenticated:

        if request.method == 'POST':
            if formulario_agragar.is_valid():
                formulario_agragar.save()

                messages.success(request, 'Contenido Agregado')
                return redirect ('home')
            
 
        # PART 13.02 - Despues de poner pass cramos la plantilla agregar.html
        return render (request, 'agregar.html', {'formulario':formulario_agragar}) 
    else:
        messages.error(request, 'Debe iniciar sesión')
        return redirect ('inicio')

# --------------------------------  PART 14 ACTUALIZAR UBICACION ----------------------------------------------#

# 14.02 EL 14.01 Esta en ubicacion.html
def actualizar_ubi_historial(request, pk):

    # 14.03 
    if request.user.is_authenticated:

        ubicacion_actual = historial.objects.get(id=pk)
        #  {POST} = Si hacen algo , {None} = Si no hacen nada  , {instance} = que aparezca el id a cambiar 
        formulario_actualizar = FormAgregar(request.POST or None, instance=ubicacion_actual)

        if formulario_actualizar.is_valid():
            formulario_actualizar.save()
            
            messages.success(request, 'Contenido Actualizado!')
            return redirect ('home')
        
        return render (request, 'actualizar.html', {'formulario_actualizar':formulario_actualizar}) 
    else:
        messages.error(request, 'Debe iniciar sesión')
        return redirect ('inicio')






    

