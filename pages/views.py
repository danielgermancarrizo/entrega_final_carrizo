from email.message import Message
from sre_constants import SUCCESS
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import PageForm
from .models import Page
from multiprocessing import context
from re import template
from unicodedata import name
from urllib import request, response
from winreg import DeleteValue
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.views.generic import TemplateView 
from typing import Any, Dict 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views import generic
# Create your views here.

class PageDeleteView(LoginRequiredMixin,DeleteView):
    model = Page
    template_name = 'page_confirm_delete.html'
    success_url = reverse_lazy('admin_page')


class PageCreate(LoginRequiredMixin,CreateView):
     model = Page
     template_name = './create_page.html'
     success_url = reverse_lazy('admin_page')      
     redirect_field_name = './list'
     fields = [
        'title',
        'content',
        'image'
     ]
     
     def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
       
class PageListView(ListView):
    model = Page 
    template_name = './list_pages.html'
    ordering = ['-creation_date']
 

class PageAdminListView(LoginRequiredMixin,ListView):
    model = Page 
    template_name = './admin.html'
    ordering = ['creation_date']
    
class PageListDetailView(DetailView):
    model = Page
    template_name = './detail_page.html'
    
class PageUpdateView(LoginRequiredMixin,UpdateView):
    model = Page
    template_name = './update_page.html'
    fields = [
        'title',
        'content',
        'image'
    ]
    success_url = reverse_lazy('admin_page')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    


