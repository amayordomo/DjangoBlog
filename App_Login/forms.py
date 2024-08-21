from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2')  # Exclude other unwanted fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

         # Remove the help text from the password fields
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        if 'usable_password' in self.fields:
            del self.fields['usable_password']
