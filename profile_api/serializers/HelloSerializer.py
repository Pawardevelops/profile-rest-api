from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    
    def validate(self, data):
        name = data.get("name")
        if name.lower() != "sachin":
            raise serializers.ValidationError("Name is not sachin")
        return data