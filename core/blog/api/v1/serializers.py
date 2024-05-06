from rest_framework import serializers

class PosTSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)