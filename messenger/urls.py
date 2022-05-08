from django.urls import path
from django.views.generic import TemplateView
from .views import MessageCreate, MessageListView, MessageDetailView, MessageDeleteView

urlpatterns = [    
               path('create/', MessageCreate.as_view(), name='message_create'),
               path('list/', MessageListView.as_view(), name='message_list'),
               path('view/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
               path('delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
               path('menu/', TemplateView.as_view(template_name="message_menu.html"), name='message_menu'),
              # path('about/', TemplateView.as_view(template_name = 'pages/templates/about.html'), name='about')
]