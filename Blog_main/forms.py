from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username','password1','password2') # password1 is for typing password and password2 for confirm password and it's default in django
        