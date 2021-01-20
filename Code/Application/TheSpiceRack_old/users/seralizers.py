from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


from . import models


# Define the data to serialize when we request a User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id', 'full_name', 'email')


# This is used when a logged in user wants their details
# PUT Requests to this are broken
class CustomUserDetailSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        model = models.CustomUser
        fields = ('id', 'email', 'full_name')
        read_only_fields = ('id', 'email', 'full_name')


# This serializer defines what we need to register users_old
class CustomRegisterSerializer(RegisterSerializer):
    full_name = serializers.CharField(required=True)


    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'full_name': self.validated_data.get('full_name', ''),
        }


    # The process for saving users_old. Any extra steps we need to do (like change fields,
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        self.cleaned_data["username"] = self.cleaned_data["email"].split('@')[0]
        user.full_name = self.cleaned_data["full_name"]

        adapter.save_user(request, user, self)

        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user
