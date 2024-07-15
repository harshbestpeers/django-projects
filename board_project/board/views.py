from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Topic, Board, Post
from django.contrib.auth.models import User
from django.db.models import Count, Max
from .forms import NewTopicForm, ReplyPostForm



class Board_main(View):
    def get(self, request):

        board_posts_count = Board.objects.annotate(
            num_posts=Count("topics__posts"),
            num_topics=Count("topics"),
            last_posts=Max("topics__posts__created_at"),
            last_post_user_name=Max("topics__posts__created_by__username"),
        ).values("id",
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
    def get(self, request, id):
        board = Board.objects.get(id=id)
        
        board_topics = (
            Board.objects.filter(id = id)
            .annotate(
                num_posts=Count("topics__posts"),
                last_posts_user_name=Max("topics__posts__created_by__username"),
            )
            .values("topics__id",
                "topics__subject",
                "topics__starter__username",
                "num_posts",
                "last_posts_user_name",
            )
        )
        print(board_topics)
        context = {"board_topics": board_topics, "board":board}
        return render(request, "topics.html", context)


# class NewTopic(View):
#     def get(self, request, id):
#         board = Board.objects.get(id=id)
#         context = {"board":board}
#         return render(request, "new_topic.html", context)

#     def post(self, request, id):
#         board = Board.objects.get(id=id)

#         subject = request.POST['subject']
#         message = request.POST['message']

#         user = User.objects.get(username="harsh")  #  get the currently logged in user

#         topic = Topic.objects.create(
#             subject=subject,
#             board=board,
#             starter=user
#         )

#         post = Post.objects.create(
#             message=message,
#             topic=topic,
#             created_by=user
#         )

#         return redirect('topics', id=board.id)  # TODO: redirect to the created topic page


class NewTopic(View):
    def get(self, request, id):
        board = Board.objects.get(id=id)
        form = NewTopicForm()
        context = {"board":board, "form":form}
        return render(request, "new_topic.html", context)

    def post(self, request, id):
        board = Board.objects.get(id=id)
        user = User.objects.get(username="harsh")
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('topics', id=board.id)
        else:
            form = NewTopicForm()


class NewPost(View):
    def get(self,request, id):

        topic = Topic.objects.get(id=id)
        posts = (topic.posts.all())
        posts = posts[::-1]

        context = {"topic":topic, "posts":posts}

        return render(request, "new_post.html", context)


class ReplyPost(View):
    def get(self,request, id):
        topic = Topic.objects.get(id=id)

        context = {"topic":topic}

        return render(request, "reply_post.html", context)

    def post(self, request, id):
        user = User.objects.get(username="harsh")
        topic = Topic.objects.get(id=id)
        message = request.POST.get("message")
        post = Post(
            message=message,
            topic=topic,
            created_by=user)
        post.save()
        context = {"topic":topic}   
        return render(request, "board.html", context)
        