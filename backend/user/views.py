from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User
from .models import FirebaseUser
from rest_framework import authentication
from rest_framework.response import Response
from firebase_admin import auth as firebase_auth
from backend.settings import firebase_app


# @permission_classes([IsAuthenticated])
class UserDestroyAPIView(generics.GenericAPIView):
    check_revoked = False

    def delete(self, request, *args, **kwargs):
        auth = authentication.get_authorization_header(request).split()
        firebase_token = auth[1].decode()
        uid = firebase_auth.verify_id_token(
            firebase_token,
            app=firebase_app,
            check_revoked=self.check_revoked,
        )["uid"]

        FirebaseUser.objects.all().filter(uid=uid).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


delete_user_view = UserDestroyAPIView.as_view()
