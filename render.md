- Creamos la base de datos en Render.com 
- Copiamos al url de la extension externa de la base de datos [  postgresql.. ]

- Creamos en parse de la base de datos 
    DATABASES ["default"] = dj_database_url.parse(  [ postgresql.. ])
```   
DATABASES = {
    'default': dj_database_url.parse(" postgresql.. ")
        # Replace this value with your local database's connection string.
        # default='postgresql://postgres:postgres@localhost/postgres',
        # conn_max_age=600

}
```

- Creamos una migracion para probar si funcioan - python manage.py migrate

- Tenemos que decirle a ovicon donde estan los archivos (staticfiles) - [urls.py] de proyecto


- Ponemos los archivo MEDIA URL y STATIC URL 

    STATIC_URL = 'static/'
    MEDIA_URL = 'media/'
