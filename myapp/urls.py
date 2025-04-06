from django.urls import path
from .views import register_user, login_user, chat_page, index, chat_api

urlpatterns = [
    path('', index, name='index'), 
    path('chat_api/', chat_api, name='chat_api'), #hatbot API route
    path('users/register/', register_user, name='register'),  #User registration API
    path('users/login/', login_user, name='login'),  #User login API
    path('chat/', chat_page, name='chat'),  #Chat page after login
    
    
]
