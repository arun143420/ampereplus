from django.contrib.auth.models import User
from django import forms
from accounts.models import Profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.utils.translation import gettext as _
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from accounts.models import ContactUs


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder':'username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','id':'myInput', 'placeholder':'password'}))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='First Name')
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=60, label='Email Address',)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2',]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.\
            update({

            'class': 'form-control',
            'id':'form',
            'placeholder': 'example@example.com',

        })
        self.fields['password1'].widget.attrs. \
            update({

            'class':'single-input',
            'name':'pass',
            'placeholder': 'password',

        })
        self.fields['username'].widget.attrs. \
            update({

            'class': 'form-control ',
            'placeholder':'username',


        })

        self.fields['password2'].widget.attrs. \
            update({

            'class': 'form-control',
            'placeholder': 'Renter Password',

        })
        self.fields['first_name'].widget.attrs. \
            update({

            'class': 'form-control',
            'placeholder': 'first name',

        })
        self.fields['last_name'].widget.attrs. \
            update({
            'class': 'form-control',
            'placeholder':'last name',


        })



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs. \
            update({

            'class': 'form-control',
            'id':'phone',
            'placeholder':'phone'



        })
        self.fields['address'].widget.attrs. \
            update({

            'class': 'form-control',
            'placeholder':'address'

        })
        self.fields['zipcode'].widget.attrs. \
            update({

            'class': 'form-control',
            'placeholder':'ZipCode',




        })
        self.fields['area'].widget.attrs. \
            update({

            'class': 'form-control',
            'placeholder':'Area'

        })
        self.fields['tc'].widget.attrs. \
            update({

            'required':'true',

        })


