from rest_framework import serializers
from .models import CustomUser, Vote, Post

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['name','email','phone_number','username']

class PostSerializer(serializers.ModelSerializer):
    poster=serializers.ReadOnlyField(source='poster.username')
    poster_id=serializers.ReadOnlyField(source='poster.id')
    class Meta:
        model = Post
        fields= ['id','title','url','poster','poster_id','created']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields= ['id']