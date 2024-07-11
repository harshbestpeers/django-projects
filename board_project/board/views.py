from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Topic, Board, Post
from django.contrib.auth.models import User
from django.db.models import Count, Max

# Create your views here.
class Main(View):
    def get(self, request):
        breakpoint()
        board_posts_count = Board.objects.annotate(
            num_posts=Count("topics__posts"),
            num_topics=Count("topics"),
            last_posts=Max("topics__posts__created_at"),
            last_post_user_name=Max("topics__posts__created_by__username"),
        ).values(
            "name",
            "num_posts",
            "description",
            "num_topics",
            "last_posts",
            "last_post_user_name",
        )

        context = {"board_posts_count": board_posts_count}
        return render(request, "board.html", context)


class BoardTopic(View):
    def get(self, request, xyz):
        board_topics = (
            Board.objects.filter(name = "Django")
            .annotate(
                num_posts=Count("topics__posts"),
                last_posts_user_name=Max("topics__posts__created_by__username"),
            )
            .values(
                "topics__subject",
                "topics__starter__username",
                "num_posts",
                "last_posts_user_name",
            )
        )

        context = {"board_topics": board_topics}
        return render(request, "topics.html", context)
