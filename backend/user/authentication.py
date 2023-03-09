from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, NotFound
from firebase_admin import auth as firebase_auth
from backend.settings import firebase_app

User = get_user_model()


class FirebaseAuthentication(authentication.BaseAuthentication):
    keyword = "Bearer"
    check_revoked = True

    def authenticate(self, request):
        auth = authentication.get_authorization_header(request).split()
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1 or len(auth) > 2:
            msg = "Invalid token."
            raise AuthenticationFailed(msg)

        try:
            firebase_token = auth[1].decode()
        except UnicodeError:
            msg = "Invalid - Token contains invalid characters."
            raise AuthenticationFailed(msg)

        return self.authenticate_credentials(firebase_token)

    def authenticate_credentials(self, firebase_token):
        try:
            decoded_token = firebase_auth.verify_id_token(
                firebase_token,
                app=firebase_app,
                check_revoked=self.check_revoked,
            )
        except (ValueError, firebase_auth.InvalidIdTokenError):
            msg = "Token is invalid."
            raise AuthenticationFailed(msg)
        except firebase_auth.ExpiredIdTokenError:
            msg = "Token expired."
            raise AuthenticationFailed(msg)
        except firebase_auth.RevokedIdTokenError:
            msg = "Token has been revoked."
            raise AuthenticationFailed(msg)
        except firebase_auth.CertificateFetchError:
            msg = "Temporarily unable to verify the token."
            raise AuthenticationFailed(msg)
        except firebase_auth.UserNotFoundError:
            msg = "User not found in firebase, please contact us"
            raise NotFound(msg)

        firebase_user_record = firebase_auth.get_user(
            decoded_token["uid"],
            app=firebase_app,
        )

        try:
            user = User.objects.get(uid=firebase_user_record.uid)
        except User.DoesNotExist:
            user = self._create_user(firebase_user_record)

        except firebase_auth.UserNotFoundError:
            msg = "No such user found"
            raise AuthenticationFailed(detail=msg)

        if user is None:
            msg = "Authentication credentials were not provided."
            raise AuthenticationFailed(msg)

        return (user, decoded_token)

    def authenticate_header(self, request):
        return self.keyword

    def _create_user(self, firebase_user_record):
        try:
            return User.objects.create_user(
                uid=firebase_user_record.uid,
                email=firebase_user_record.email,
                display_name=firebase_user_record.display_name,
            )
        except IntegrityError as e:
            raise AuthenticationFailed(e.args)