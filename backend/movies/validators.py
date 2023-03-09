from rest_framework.validators import UniqueValidator
from .models import Movies

unique_game_title = UniqueValidator(queryset=Movies.objects.all(), lookup='iexact')