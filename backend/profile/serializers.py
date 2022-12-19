from .models import Profile, Consumer, Store
from rest_framework import serializers
from django.http import JsonResponse
class ProfileSerializer(serializers.ModelSerializer):
        def create(self, validated_data):
                user = Profile.objects.create_user(
                email = validated_data['email'],
                username = validated_data['name'],
                password = validated_data['password'],
                phone = validated_data['phone'],
                type = validated_data['type'],
                created_at = validated_data['created_at']
                )
                return user
        class Meta:
                model = Profile
                fields = "__all__"
        
class ConsumerSerializer(serializers.ModelSerializer):
        class Meta:
                model = Consumer
                fields = "__all__"
        
class StoreSerializer(serializers.ModelSerializer):
        class Meta:
                model = Store
                fields = "__all__"

# api/serializers.py
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate

# 회원가입
# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "username", "password")
#         extra_kwargs = {"password": {"write_only": True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             validated_data["username"], None, validated_data["password"]
#         )
#         print(user)
#         return user
        # return JsonResponse(user)


# 접속 유지중인지 확인
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "username")


# 로그인
# class LoginUserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Unable to log in with provided credentials.")