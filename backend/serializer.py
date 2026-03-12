from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Register
from .models import Post,Comment



class Register_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['username','email','password']

    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)
    

# ________________________ Blog APi _________________
class Comment_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
class Post_serilizer(serializers.ModelSerializer):
    comment=Comment_serilizer(many=True,read_only=True)

    class Meta:
        model=Post
        fields='__all__'
