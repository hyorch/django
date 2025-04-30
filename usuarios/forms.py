from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model() # settyngs.py AUTH_USER_MODEL
        fields = (
            'email',
            'username'
        ) # password viene por defecto


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # settyngs.py AUTH_USER_MODEL
        fields = (
            'email',
            'username'
        ) # password viene por defecto



