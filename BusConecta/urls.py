
""" URL por defecto de django """


from django.contrib import admin
from django.urls import path, include

# Render - Decirle donde estan  los archvos estaticos 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppBussConecta.urls'))
]


# Render 
urlpatterns+= staticfiles_urlpatterns()