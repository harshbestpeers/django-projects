from django.urls import path
from .views import *

urlpatterns = [
    path("", Main.as_view(), name="main"),
    path("Topics/<str:xyz>/", BoardTopic.as_view(), name="topics")
]