from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):

    """ Test API view """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):

        """ Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as function(get, post, put, patch, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview })

    def post(self,request):
        """ create a hello message with our name """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello{name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle a partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self,request,pk=None):
        """ delete an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API viewSet """

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """ Return a Hello message """
        a_viewset = [
            "Uses actions(list, create, retrive, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]
        return Response({'message':'Hello!', 'a_viewset': a_viewset})

    def create(self,request):
        """ Create a new hello message """
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        """ Handle getting an object by its ID """
        return Response({'http-method': 'GET'})

    def update(self, request, pk=None):
        """ Handle updating an object"""
        return Response({'http-method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handle updating part of an object """
        return Response({'http-method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Handle removing an object"""
        return Response({'http-method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):

    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
