from django.urls import path
#Imports views
from .views import register_user, login_user, chat_page, index  


urlpatterns = [
    path('', index, name='index'), 
    path('users/register/', register_user, name='register'),  #User registration API
    path('users/login/', login_user, name='login'),  #User login API
    path('chat/', chat_page, name='chat'),  #Chat page after login
]



