from rest_framework import serializers

class ChallengeSerializer(serializers.Serializer):

    items = serializers.CharField(max_length=40)