import django
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    return Response("Django " + django.get_version(), status=200)
