from rest_framework import serializers

from account.models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, write_only=True, required=True)
    password_confirm = serializers.CharField(min_length=4, write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password', 'password_confirm')

    def validate(self, attrs):
        password_confirm = attrs.pop('password_confirm')
        if not password_confirm == attrs['password']:
            raise serializers.ValidationError('Passwords don\'t match')
        return attrs

    @staticmethod
    def validate_first_name(value):
        if not value.istitle():
            raise serializers.ValidationError('First name should start with capital letter')
        return value

    @staticmethod
    def validate_last_name(value):
        if not value.istitle():
            raise serializers.ValidationError('Last name should start with capital letter')
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'],
                                         first_name=validated_data['first_name'],
                                         last_name=validated_data['last_name'],
                                         password=validated_data['password'],)
        user.save()
        return user
