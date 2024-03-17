from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User


class UserSeralizer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['username','email']





class CommentSerializer(serializers.ModelSerializer):

    user = UserSeralizer(read_only=True)


    class Meta:
        model = Comment
        fields = "__all__"

    





