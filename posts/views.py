from django.shortcuts import render
from rest_framework import generics, mixins, permissions,status
from rest_framework.response import Response
from .models import Post,Vote
from .serializers import PostSerializer, VoteSerializer
from rest_framework.exceptions import ValidationError

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class= PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

class VoteCreate(generics.CreateAPIView,mixins.DestroyModelMixin):
    serializer_class= VoteSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        post=Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user,post=post)
        
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError("You have already voted for the post... :)")
        serializer.save(voter=self.request.user,post=Post.objects.get(pk=self.kwargs['pk']))
    
    def delete(self,request,*args,**kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_201_NO_CONTENT)
        else:
            raise ValidationError("You have not voted for this....")

class PostRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def delete(self,request,*args,**kwargs):
        post=Post.objects.filter(pk=kwargs['pk'],poster=self.request.user)
        if post.exists():
            self.destroy(request, *args,**kwargs)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError ("This is not your post, and You can't delete bro......")


