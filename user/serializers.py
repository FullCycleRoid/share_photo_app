from django.contrib.auth import authenticate
from rest_framework import serializers
from main.models import AdvancedUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancedUser
        fields = ('phone', 'first_name', 'surname', 'password')

    def create(self, validated_data):
        return AdvancedUser.objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        phone = attrs.get('phone')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            phone=phone,
            password=password
        )
        if not user:
            msg = 'Unable to authenticate with provided credentials'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancedUser
        fields = ('id', 'phone', 'first_name', 'surname')
