from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Topic
from .serializer import TopicSerializer

@api_view(['GET'])
def topic_list(request):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    return Response(serializer.data)
