from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.topic_list),
    # path('post/', views.postTopic),
]