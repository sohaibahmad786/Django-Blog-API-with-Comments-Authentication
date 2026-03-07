from rest_framework import serializers
from .models import Student
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import Register
from .models import Note
from .models import Category
from .models import Products

class Student_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
    extra_kwargs={
        'created_at':{'read_only':True}
    }
    extra_kwargs={
       'email':{
           'required':True,
           'allow_blank':False,
           'error_messages':{
               'required':"please enter email",
               'allow_blank':"Email are compulsory"
           }
       }
       
    }
    def validate_age(self,value):
        if value < 5:
            raise serializers.ValidationError("You are now Child")
        return value
    def validate_course(self,value):
        if not value:
            raise serializers.ValidationError("Please Choose Course")
        return value


# class Account_serilizer(serializers.ModelSerializer):
#     class Meta:
#         model=Account
#         fields=['full_name','username','email','password','age']
#         extra_kwargs={
#          'username':{
#              'required':True,'allow_blank':False,
#              'error_messages':{
#                  'required':"please Enter username",
#                  'allow_blank':"please Enter Password"
#              }
#          },
#          'password':{
#              'required':True, 'allow_blank':False,
#              'error_messages':{
#                  'required':"please Enter Password",
#                  'allow_blank':"please Enter Password",
#              }
#          }
#         }

#     def validate_password(self,value):
#         if len(value)<8:
#             raise serializers.ValidationError("Please Enter Strong Password minimium 8 chars")
#         return value
    
#     def validate_age(self,value):
#         if value < 18:
#             raise serializers.ValidationError("Sorry your age is not now to make account")
#         return value
    
#     def create(self,validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         return super().create(validated_data)
#     def update(self,instance,validated_data):
#         validated_data['password']=make_password(validated_data['password'])
#         return super().update(instance,validated_data)
    


class Register_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['username','email','password']

    def create(self, validated_data):
        validated_data['password']=make_password(validated_data['password'])
        return super().create(validated_data)
    
class Note_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields='__all__'
        read_only_field=['user']

# ____________________ product APi___________________
class category_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class products_serilizer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than zero')
        return value
    def validate_stock(self,value):
        if value == 0:
            raise serializers.ValidationError("Stck must be greater than zero")
        return value
    def validate_name(self,value):
        if Products.objects.filter(name=value).exists():
            raise serializers.ValidationError("Product with this name is already present")

