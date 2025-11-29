from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import request
from rest_framework import status
from profile_api.serializers.HelloSerializer import HelloSerializer
from rest_framework import serializers

class Sanitize():
    def __init__(self, serializer_class, data, partial=False):
        self.serializer_class = serializer_class
        self.data = data
        self.partial = partial
    
    def sanitize(self):
        serializer = self.serializer_class(data=self.data, partial=self.partial)
        if not serializer.is_valid():
            print("not valid")
            raise serializers.ValidationError(serializer.errors)
        return serializer.validated_data
    


class HelloApiView(APIView):
    serializer_class = HelloSerializer
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "Uses HTTP methods as functions (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your logic",
            "Is mapped manually to URLs",
        ]
        return Response({"message": "Hello, World!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        sanitized_data = Sanitize(self.serializer_class, request.data).sanitize()
        return Response({"message": "Hello, World!", "name": sanitized_data.get("name")})    
        
    def put(self, request, pk=None):
        """Handle updating an object"""
        sanitized_data = Sanitize(self.serializer_class, request.data).sanitize()
        print(sanitized_data)
        return Response({"message": "Hello, World!", "name": sanitized_data.get("name")})

    def patch(self, request, pk=None):
        """Handle partial updating an object"""
        sanitized_data = Sanitize(self.serializer_class, request.data).sanitize()

        return Response({"message": "Hello, World!", "name": sanitized_data.get("name")})
    
    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({"message": "Hello, World!", "name": "sachin"})