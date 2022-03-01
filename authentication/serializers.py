from authentication.models import User

from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=8)
    email = serializers.EmailField(max_length=100)
    phone_number = PhoneNumberField(allow_null=True, allow_blank=True)
    password = serializers.CharField(min_length=2)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number','password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        email_exists = User.objects.filter(email=attrs['email']).exists()
        phone_number_exists = User.objects.filter(phone_number=attrs['phone_number']).exists()


        if username_exists:
            raise serializers.ValidationError(detail="Username already exists.")

        if email_exists:
            raise serializers.ValidationError(detail="Email already exists.")

        # if phone_number_exists:
        #     raise serializers.ValidationError(detail="Phone number already exists.")

        return super().validate(attrs)