from django.urls import path
from . import views

# /api/movies/
urlpatterns = [
    path('', views.MoviesListCreateAPIView.as_view(), name='movies-list'),
    path('<int:pk>/', views.MoviesDetailAPIView.as_view(), name='movies-detail'),
    path('<int:pk>/update/', views.MoviesUpdateAPIView.as_view(), name='movies-update'),
    path('<int:pk>/delete/', views.MoviesDestroyAPIView.as_view(), name='movies-delete')

]