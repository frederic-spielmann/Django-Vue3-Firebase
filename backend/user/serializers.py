from rest_framework import serializers


class UserPublicSerializer(serializers.Serializer):
    display_name = serializers.CharField(read_only=True)