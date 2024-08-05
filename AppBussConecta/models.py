from django.db import models


# 7.04-1 - Para  poner limite a los numero
# from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


#PART 7.01 - modelo de HISTORIAL O INFORMACION
class historial(models.Model):

    # 7.02 historial o informaicon de la fecha , para saber la hora que se ha creado 
    tiempo_creado = models.DateTimeField(auto_now_add=True)

    # 7.03 Todo loque queremos guardar 
    inicio = models.CharField(max_length=50)
    final = models.CharField(max_length=50)
    # --------------------- NUEVO SISTEMA ------------------
    poste_1 = models.CharField(max_length=5)
    poste_2 = models.CharField(max_length=5)
    poste_3 = models.CharField(max_length=5)

        # 7.04 Pongo IntegerField() porque exite : son los numeros de postes
        # 7.04 Validator funciona como rangos 
        # 7.04 Campos NO OBLIGATORIOS - 
            # blank=True: Permite que el campo esté vacío en los formularios.
            # null=True: Permite que el campo tenga un valor nulo en la base de datos.
    # poste_1 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    # poste_2 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)], blank=True, null=True)
    # poste_3 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)], blank=True, null=True)
    


        # 7.05  notas 
    notas =  models.CharField(max_length = 500, blank=True, null=True )


    # 7.06 : Devolver lo que queremos mostrar en la pantalla 
    def __str__(self):
        return (f'{self.inicio} {self.final} {self.poste_1} {self.poste_2}')




# 7.07 HACER UNA MIGRACION - CMD :  python manage.py makemigrations - python manage.py migrate

# 7.08 AÑADIR historial al admin.py 

