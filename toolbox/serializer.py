from rest_framework import serializers

class TopicSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    created_on = serializers.DateTimeField()
    updated_on = serializers.DateTimeField()

