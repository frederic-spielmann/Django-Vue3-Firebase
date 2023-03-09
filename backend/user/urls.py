from django.urls import path
from . import views

# /api/user/
urlpatterns = [
    path('', views.delete_user_view),
]
