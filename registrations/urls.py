from django.urls import path
from django.views.generic import TemplateView
from .views import (AccountLoginView, ProfileUpdate, register_request, 
                    UserView, change_password, EditUserView, 
                    PasswordChangeView, UserRegisterView) 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', UserRegisterView.as_view(), name='signup'),
    path('login/',AccountLoginView.as_view(), name = 'login'),
    path('profile/', ProfileUpdate.as_view(), name='edit_profile'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name="logout"),   
    path('edit-account/', EditUserView.as_view(), name='edit_account'),
    path('change-password/', views.change_password, name='change_password'),
    # path('edit/', EditUserView.as_view(), name='edit'),
    path('password-change/', PasswordChangeView.as_view(), name = 'change' ),
    path('menu-profile/', TemplateView.as_view(template_name="menu_profile.html"), name='menu_profile'),
             
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)