from .models import Student
from .serializers import StudentSerializer 
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from api3.throttling import perticular




class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]   
    permission_classes=[IsAuthenticatedOrReadOnly]  
    #for same no of access for all class (it is global)
    # throttle_classes=[AnonRateThrottle,UserRateThrottle]

    
    #for diffrent no of access for diffrent class 
    #step 1:created file throttling.py 
    #step 2:mention in setting no of access
    #step 3:in views import function (ex:from api3.throttling import perticular) 
    throttle_classes=[AnonRateThrottle,perticular]


