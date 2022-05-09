from audioop import reverse
from re import template
from tkinter.tix import Form
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from requests import request
from .forms import ChangeUserPasswordForm, NewUserForm, UserCreationForm, UserRegisterForm
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, 
                                       UserChangeForm, PasswordChangeForm)
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django import forms
from .forms import NewUserForm,ProfileUpdateForm,ProfileForm, EditUserForm, ChangeUserPasswordForm, FormularioLogin
from .models import Profile
from django.contrib import messages
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache



# class AccountLoginView(TemplateView):
#     template_name = 'login.html'
    
#     def get(self,request):
#         context = {
#             'form': AuthenticationForm()
#         }
#         return render(request,self.template_name, context)
    
#     def post(self,request):
#         form = AuthenticationForm(request,data=request.POST)
        
#         if form:
#             user = request.POST.get('username')
#             password = request.POST.get('password')
#             user_auth = authenticate(username = user, password=password)
            
#             if user_auth:
#                 login(request,user_auth)
#                 return render(request,self.template_name,context={'message': f'Bienvenidx {user}'})
#             else:
#                 return render(request,self.template_name,context={'message': 'Error, verifique usuario y contraseña.'})
#         else:
#             return render(request,self.template_name,context={'message': 'Formulario con error'})     

class AccountLoginView(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args , **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(AccountLoginView, self).dispatch(request,*args, **kwargs)
    
    def form_valid(self,form):
        login(self.request, form.get_user())
        return super(AccountLoginView, self).form_valid(form)
    

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('menu_profile')
    template_name = 'edit_profile.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
              
   
# def register(request):
#      if request.method == 'POST':
#          form = UserRegisterForm(request.POST) 
#          if form.is_valid():
#              form.save() 
#              username = form.cleaned_data.get('username') 
#              messages.success(request, f'Your account has been created! You are now able to log in') 
#              return redirect('login')
#      else:
#          form = UserRegisterForm()
#      return render(request, 'users/register.html', {'form': form}) 
  

class UserCreationFormCustom(UserCreationForm):
    
    def save (self, commit: bool = True) -> User:
        user = User.objects.create(
            username=self.data['username'],
            email = self.data['email'],
            password=self.data['password1'],
        )
        return user

class UserCreationFormCustom(UserCreationForm):
    def save(self, commit: bool = True) -> User:
        user = User.objects.create(
            username=self.data['username'],
            password=self.data['password1'],
        )
        return user

class UserChangeFormCustom(UserChangeForm):
          
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

class UserView(LoginRequiredMixin, TemplateView):
    template_name = "edit.html"

    def get(self, request):
        context = {
            'form': UserChangeFormCustom(
                initial={
                    'email': request.user.email,
                    'username': request.user.username,
                }
            )
        }
        return render(request, self.template_name, context)


    def post(self, request):
        
        form = UserChangeFormCustom(request.POST)
        if form.is_valid():
            user_update_info = form.cleaned_data
            user = request.user
            user.email = user_update_info.get('email')
            user.password1 = user_update_info.get('password1')
            user.password2 = user_update_info.get('password2')
            user.save()

            context = {
                    'form': UserChangeFormCustom(
                        initial={
                            'email': request.user.email
                        }
                    )
            }
        print(form.errors)
        
        return render(request, self.template_name, context)
     
class PasswordChangeView(PasswordChangeView):
    form_class= ChangeUserPasswordForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'password_success.html', {})
    
          
@login_required   
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'El password fue actualizado correctamente')
            return redirect('menu_profile')
        else:
            messages.error(request, 'Se produjo un error al actualizar el password, verifique.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

class EditUserView(UpdateView):
    form_class = EditUserForm
    template_name = 'edit.html'
    
    success_url = reverse_lazy('menu_profile')
    
    def get_object(self):
        return self.request.user 
       

class UserRegisterView(CreateView):
    form_class= UserRegisterForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Proceso de registro finalizado exitosamente." )
            return redirect("login")
            messages.error(request, "Falló el registro.")
 	
    return render (request=request, template_name="signup.html", context={"register_form":form})    
