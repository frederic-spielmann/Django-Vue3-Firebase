from django.urls import path
from . import views
# from .views import api_home


urlpatterns = [
    path('', views.api_home)  # localhost:8000/api/
    # path('auth/register/'),  # to create a new account
]