from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog
class BlogSerializer(serializers.ModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model=Blog
        fields='__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']
        extra_kwargs={'password':{'write_only':True}}
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
