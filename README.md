# Control Cambustible - django

Aplicación Django para el control de combustible.


Ejecutar en local
```bash
manage.py runserver 0.0.0.0:8080
```

Docker Built Image
```bash
docker build -t ctr-combustible .
docker run -d -p 8080:8080 --rm --name ctr-combustible ctr-combustible
```


Docker-Compose Imagen Local
```bash
docker-compose up -d
```

## Develop

```bash
#add app
docker exec -it web bash
python manage.py startapp usuarios
docker-compose exec web python manage.py startapp usuarios # Alternativa

python manage.py showmigrations
python manage.py makemigrations usuarios
python manage.py migrate

python manage.py createsuperuser

# ejecutar tests
python manage.py tests
```


https://gitlab.com/debsdaniel/djpro_ctrl_comb/-/tree/main?ref_type=heads

