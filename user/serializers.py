from rest_framework import serializers
from .models import UserAPI

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAPI
        fields = ('username', 'email', 'gender')



class UserCreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserAPI
        fields = ('username', 'password', 'email', 'gender')



