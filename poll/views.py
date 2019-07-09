# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from poll import models
from poll import serializers
from django.contrib.auth import authenticate
from poll import permissions as poll_permissions
from rest_framework import permissions
from rest_framework import exceptions


class PollList(generics.ListCreateAPIView):
    serializer_class = serializers.PollSerializer
    queryset = models.Poll.objects.all()
    #permission_classes = [permissions.IsAuthenticated, poll_permissions.IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PollSerializer
    queryset = models.Poll.objects.all()  
    permission_classes = [permissions.IsAuthenticated, poll_permissions.CanEditPost]



class ChoiceList(generics.ListCreateAPIView):
    serializer_class = serializers.ChoiceSerializer
    queryset = models.Choice.objects.all()
    #permission_classes = [permissions.IsAuthenticated, poll_permissions.CanEditChoice]


    def post(self, request, format=None):
        poll = models.Poll.objects.get(id=request.data.get('poll'))
        if poll and poll.created_by != request.user:
            raise exceptions.PermissionDenied('You do not have sufficient permissions')

        serializer = serializers.ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ChoiceSerializer
    queryset = models.Choice.objects.all() 
 


class VoteList(generics.ListCreateAPIView):
    serializer_class = serializers.VoteSerializer
    queryset = models.Vote.objects.all()


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.VoteSerializer
    queryset = models.Vote.objects.all()
          



class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
