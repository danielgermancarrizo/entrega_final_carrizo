from pyexpat import model
from django import forms
from redis import AuthenticationError
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm


class ProfileForm(forms.ModelForm):
     class Meta:
         model = Profile
         fields = ['avatar', 'description', 'url_web']
         widgets = {
             'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
             'description': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
             'url_web': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
         }

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    def save(self,commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserRegisterForm(UserCreationForm):
     email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
     password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
     password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
         
     
     class Meta:
         model = User
            
         fields = ['username', 'email', 'password1','password2']

# # Create a UserUpdateForm to update username and email
# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
    
#     class Meta:
#         model = User
#         fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    description = forms.CharField(max_length=200)
    class Meta:
        model = Profile
        fields = ['description','avatar']
        
class EditUserForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    # is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'email')

class ChangeUserPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type': 'password'}))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1','new_password2')
        
class FormularioLogin(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Contraseña'
        