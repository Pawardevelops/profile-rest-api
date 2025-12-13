from rest_framework import serializers
from profile_api.models import ProfileFeeditem

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeeditem
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}

    def create(self, validated_data):
        """create and return new validated user"""
        print(validated_data)
        user_profile = validated_data['user_profile']
        status_text = validated_data['status_text']
        return ProfileFeeditem.objects.create(user_profile=user_profile, status_text=status_text)