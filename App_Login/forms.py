from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2')  # Only include these fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove help text from fields
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        # Optionally remove 'usable_password' field if present
        if 'usable_password' in self.fields:
            del self.fields['usable_password']
