from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# desde el archivo forms.py
from .forms import CustomUserCreationForm, CustomUserChangeForm



UsuarioPersonalizado = get_user_model() # settings.py AUTH_USER_MODEL

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UsuarioPersonalizado
    list_display = [
        'email',
        'username',
        'is_superuser'
    ]


# Registrar usuario person
admin.site.register(UsuarioPersonalizado, CustomUserAdmin)
 
