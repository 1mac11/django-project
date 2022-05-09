from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer  # noqa

User = get_user_model()


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if not password:
            raise ValidationError('password is required')
        if not password2:
            raise ValidationError('password2 is required')

        if password != password2:
            raise ValidationError('password and password2 are not match')

        attrs.pop('password2')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_name', 'first_name', 'email', 'phone',)


class AccessTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # TODO: add user data when generating token for user
        token['user'] = user.email

        return token
