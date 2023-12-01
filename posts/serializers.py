from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username' ,'email']




class PostSerializers(serializers.ModelSerializer):
    author = UserSerializer
    category = serializers.StringRelatedField()
    class Meta:
        model = Post
        fields = '__all__'