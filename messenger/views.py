from django.shortcuts import render
from requests import request
from .models import Message
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MessageCreate(LoginRequiredMixin,CreateView):
     model = Message
     template_name = 'message_create.html'
     success_url = reverse_lazy('message_menu')      
     redirect_field_name = './templates/message_create.html'
     fields = [
        'title',
        'content',
        'receiver'
        ]
     
     def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

class MessageListView(LoginRequiredMixin,ListView):
    model = Message
    template_name = 'message_list.html'
    ordering = ['-created']
       

class MessageDetailView(LoginRequiredMixin,DetailView):
    model = Message
    template_name = './message_detail.html'
    
    
class MessageDeleteView(LoginRequiredMixin,DeleteView):
    model = Message
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy('message_list')