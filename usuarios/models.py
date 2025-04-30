from django.db import models
# Extender AbstractUser para crear un modelo de usuario personalizado
from django.contrib.auth.models import AbstractUser

#             heredar de AbstractUser
class Usuario(AbstractUser):
    ... # Heredear sin cambiar nada



