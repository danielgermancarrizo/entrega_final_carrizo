from django.urls import path
from django.views.generic import TemplateView
from .views import (PageCreate, PageListView, PageListDetailView, PageUpdateView, PageAdminListView, 
                    PageDeleteView)

urlpatterns = [    
               path('crear/', PageCreate.as_view(), name='create_page'),
               #path('list/', PageListView.as_view(), name='list_page'),
               path('admin/', PageAdminListView.as_view(), name='admin_page'),
               path('detail/<int:pk>', PageListDetailView.as_view(), name = 'detail_page'),
               path('update/<int:pk>', PageUpdateView.as_view(), name = 'update_page'),
               path('delete/<int:pk>', PageDeleteView.as_view(), name = 'delete_page'),
               
              # path('about/', TemplateView.as_view(template_name = 'pages/templates/about.html'), name='about')
]