from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        contributor_group, _ = Group.objects.get_or_create(name='Contributor')
        user.groups.add(contributor_group)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email

        if user.is_staff or user.groups.filter(name='Admin').exists():
            token['role'] = 'Admin'
        elif user.groups.filter(name='Viewer').exists():
            token['role'] = 'Viewer'
        else:
            token['role'] = 'Contributor'

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        role = 'Admin' if (user.is_staff or user.groups.filter(name='Admin').exists()) else (
            'Viewer' if user.groups.filter(name='Viewer').exists() else 'Contributor'
        )
        data['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': role,
        }
        return data
