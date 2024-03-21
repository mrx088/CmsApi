from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User


class UserSeralizer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['username','email']





class CommentSerializer(serializers.ModelSerializer):

    user = UserSeralizer(read_only=True)
    created = serializers.DateTimeField(format="%d-%m-%Y")
    hour = serializers.DateTimeField(format="%H:%M:%S")


    class Meta:
        model = Comment
        fields = "__all__"

    





