from rest_framework import serializers

class HelloSerializer(serializers.Serializer):

    """serializes a name field to for testing our APIView """
    name = serializers.CharField(max_length = 10)
    
