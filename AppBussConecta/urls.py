""" url de App Buss Conecta """


from django.urls import path

from . import views

'''
# Tambien se puede identificar donde importar views
# from appwebsite import views
'''


urlpatterns = [
    # url home
    path('home', views.home , name='home'),
    # inicio - 
    path('', views.inicio , name='inicio'),

    # PART 4 
    path('iniciar_sesion', views.iniciar_sesion , name='iniciar_sesion'),
    # PART 5
    path('cerrar_sesion', views.cerrar_sesion , name='cerrar_sesion'),
    # PART 6
    path('registro', views.registro_user , name='registro'),
    # PART 10.01 - Ubicacion : porque quiero que en la URL apareza (.../ubicacion/1)
    path('ubicacion/<int:pk>', views.historial_ubicacion, name='ubicacion'),
    # PART 12
    path('borrar/<int:pk>', views.borrar_ubi_historial , name='borrar'),
    # PART 13
    path('agregar', views.agregar_ubi_historial , name='agregar'),
    # PART 14
    path('actualizar/<int:pk>', views.actualizar_ubi_historial , name='actualizar'),
    
]
