from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, \
    ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, CommentSerializer
from .models import User
from properties.models import Comment, Property
from django.http import JsonResponse

# Create your views here.
class UserCreate(CreateAPIView):
    serializer_class = UserSerializer

class UserGetSet(RetrieveAPIView, UpdateAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return get_object_or_404(User, id=self.kwargs['pk'])

class CommentCreateUser(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, object_id=self.kwargs['pk'])

class CommentCreateProperty(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, object_id=self.kwargs['pk'], endOfCommentChain=True)
        instance = serializer.save()
        
        # set the new end of comment chain
        if (instance.replyingTo != None):
            comm = Comment.objects.get(commentID=instance.replyingTo)
            comm.endOfCommentChain = False
            comm.save()
    
class CommentListUser(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    def get_queryset(self):
        return Comment.objects.filter(object_id=self.kwargs['pk'], content_type = 6) # content type = 6 is user comment

class CommentListProperty (APIView):

    permission_classes = [IsAuthenticated]
    
    def get (self, request, pk):
        prop = Property.objects.get(id=self.kwargs['pk'])        
        propEnds = prop.reviews.filter(endOfCommentChain=True)
        print(propEnds.all())

        big_array = []
        for i in propEnds:
            temp_array = [i]
            if (i.replyingTo != None):
                currentComment = Comment.objects.get(commentID=i.commentID)
                while (currentComment.replyingTo != None):
                    currentComment = Comment.objects.get(commentID=i.replyingTo)
                    temp_array.append(currentComment)
            
            temp_array = temp_array[::-1]
            serializer = CommentSerializer(temp_array, many=True)
            big_array.append(serializer.data)

        print(big_array)
        return JsonResponse(big_array, safe=False)