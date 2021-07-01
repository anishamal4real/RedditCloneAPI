from rest_framework import serializers
from .models import CustomUser, Vote, Post

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['name','email','phone_number','username']

class PostSerializer(serializers.ModelSerializer):
    poster=serializers.ReadOnlyField(source='poster.username')
    poster_id=serializers.ReadOnlyField(source='poster.id')
    votes=serializers.SerializerMethodField()
    def get_votes(self,post):
        return Vote.objects.filter(post=post).count()
    class Meta:
        model = Post
        fields= ['id','title','url','poster','poster_id','created','votes']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields= ['id']