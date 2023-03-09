from rest_framework import serializers

from user.serializers import UserPublicSerializer
from .models import Movies
from . import validators


class MoviesSerializer(serializers.ModelSerializer):
    created_by = UserPublicSerializer(source='user', read_only=True)
    title = serializers.CharField(validators=[validators.unique_game_title])

    class Meta:
        model = Movies
        fields = [
            'id',
            'title',
            'description',
            'created_at',
            'category',
            'created_by'
        ]
        ordering = ['-id']