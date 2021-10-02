from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('firs_name', 'last_name', 'username', 'email', 'password')

        def validate(self, args):
            email = args.get('email', None)
            username = args.get('username', None)
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({'email': ('email already exists')})
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError({'username': ('username already exists')})
            return super().validate(args)

        def create(self, validate_date):
            return User.objects.create_user(**validate_date)