from rest_framework import serializers
from profile_api.models import UserProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True,'style':{'input_type':'password'}}}

    def validate(self, data):
        """validate the data"""
        # name = data.get("name")
        # if name.lower() != "sachin":
        #     raise serializers.ValidationError("Name is not sachin")
        # email = data.get("email")
        # if email.lower() != "sachin@yopmail.com":
        #     raise serializers.ValidationError("Email is not sachin@yopmail.com")
        # password = data.get("password")
        # if password.lower() != "sachin":
        #     raise serializers.ValidationError("Password is not sachin")
        return data

    def update(self, instance, validated_data):
        """update and return an existing object"""
        instance.name = validated_data.get("name", instance.name)
        instance.email = validated_data.get("email", instance.email)
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance

    def create(self, validated_datta):
        """create and return new validated user"""
        user = UserProfile.objects.create_user(
            email=validated_datta['email'],
            name=validated_datta['name'],
            password=validated_datta['password']
        )
        return user