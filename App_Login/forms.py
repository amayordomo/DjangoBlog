from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Only include these fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove help text from fields
        self.fields['username'].help_text = None
        self.fields['email'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        # Optionally remove 'usable_password' field if present
        if 'usable_password' in self.fields:
            del self.fields['usable_password']

class CustomUserChangeProfile(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')  # Only include these fields