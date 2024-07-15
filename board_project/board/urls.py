from django.urls import path
from .views import *

urlpatterns = [
    # path("", Main.as_view(), name="main"),
    path("", Board_main.as_view(), name="board"),
    path("Topics/<int:id>/", BoardTopic.as_view(), name="topics"),
    path("NewTopic/<int:id>/", NewTopic.as_view(), name="new_topic"),
    path("NewPost/<int:id>/", NewPost.as_view(), name="new_post"),
    path("ReplyPost/<int:id>/", ReplyPost.as_view(), name="reply_post")
]