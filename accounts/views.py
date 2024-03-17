from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import Comment
class AllUsers(APIView):
    def get(self,request):
        return Response({'MEssage':"WORKED"})
    



class AllComments(APIView):
    def get(self,request):
        comments = Comment.objects.all()
        SrzData = CommentSerializer(instance=comments,many=True)
        return Response(SrzData.data)