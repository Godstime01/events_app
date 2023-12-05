from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group

from .models import CustomUserModel


class RegistrationForm(UserCreationForm):

    CHOICES = (
        ('PARTICIPANT', 'PARTICIPANT'),
        ('ORGANISER', ' ORGANISER')
        )
    
    account_type = forms.ChoiceField(choices=CHOICES, required=False)
    def __init__(self, *args,  **kwargs):
        super().__init__(*args, **kwargs)

        counter = 0

        for visible in self.visible_fields():
           
           
            visible.field.widget.attrs['class'] = 'rounded-md w-full shadow block my-2'
            visible.field.widget.attrs['placeholder'] = visible.field.label

            if counter > 2:
                visible.field.widget.attrs['class'] =  'rounded-md w-full shadow border block my-2 col-span-full'
            
            counter += 1

    class Meta:
        model = CustomUserModel
        fields = ( 'username', 'email','account_type', 'password1', 'password2')


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
           
            visible.field.widget.attrs['class'] = 'rounded-md w-full shadow border block my-2'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    

    class Meta:
        model = User
        fields = '__all__'
