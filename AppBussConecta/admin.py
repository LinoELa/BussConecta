from django.contrib import admin

# 7.08 AÑADIR historial al admin.py 
from .models import historial



# Register your models here.

# 7.09 registrar models para  que se vea en le admin

admin.site.register(historial)
