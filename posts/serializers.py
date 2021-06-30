from rest_framework import serializers
from .models import CustomUser, Vote, Post

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['name','email','phone_number','username']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields= ['id','title','url','poster','created']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields= '__all__'