from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')        