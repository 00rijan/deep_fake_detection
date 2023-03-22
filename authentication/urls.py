from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register_request, name='register'),
    path('history/', views.history, name='history'),
       
]
