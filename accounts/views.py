from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import Comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated





class AllUsers(APIView):
    def get(self,request):
        return Response({'MEssage':"WORKED"})
    



class AllComments(APIView):
    def get(self,request):
        comments = Comment.objects.all()
        SrzData = CommentSerializer(instance=comments,many=True)
        return Response(SrzData.data)
    
class DeleteComment(APIView):
    def delete(self,request,pk):
        get_object_or_404(Comment,pk=pk).delete()
        return Response({"Message":"Comment deleted"})
    
class UpdateComment(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,pk):
        comment=get_object_or_404(Comment,pk=pk)
        SrzData = CommentSerializer(instance=comment,data=request.data,partial=True)
        if SrzData.is_valid():
            cd = SrzData.validated_data
            cd['user'] = request.user
            SrzData.save()
            return Response(SrzData.data)
        return Response(SrzData.errors)
    
class CreateComment(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        SrzData = CommentSerializer(data=request.POST)
        if SrzData.is_valid():
            cd = SrzData.validated_data
            cd['user'] = request.user
            SrzData.save()
            return Response(SrzData.data)
        return Response(SrzData.errors)
