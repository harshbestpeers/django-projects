from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField("board_ name", max_length=30, unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = "new_Board"


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_update = models.DateField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="topics")
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topics")


class Post(models.Model):
    message = models.TextField(max_length=40000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="+"
    )


from django.db import models
from django.contrib.postgres.indexes import GinIndex

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()
    tags = models.CharField(max_length=100)

    