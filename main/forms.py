from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

class UserName(forms.Form):
    user_name = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data = super(UserName, self).clean()
        user_name = cleaned_data.get('user_name')
