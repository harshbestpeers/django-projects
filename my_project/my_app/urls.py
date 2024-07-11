from django.urls import path
from .views import *


urlpatterns = [
    path("", Main.as_view(), name="main"),
    # path('my_member/', MyMember.as_view(), name='my_member'),
    # path("my_member/details/<int:id>", Details.as_view(), name="details"),
    path("delete/<int:id>/", Delete.as_view(), name="delete"),
    path("update/<int:id>/", Update.as_view(), name="update"),
    path("curd_operation/", CurdOperation.as_view(), name="curd"),
    path("edit/<int:id>/", Edit.as_view(), name="edit"),
    path("AddMember/", AddMember.as_view(), name="add"),
]
