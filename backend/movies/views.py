from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Movies
from .serializers import MoviesSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


@permission_classes([IsAuthenticated])
class MoviesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

    def perform_create(self, serializer):
        print(serializer)
        serializer.save(user=self.request.user)


class MoviesDetailAPIView(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class MoviesUpdateAPIView(generics.UpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.description = instance.title


class MoviesDestroyAPIView(generics.DestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
