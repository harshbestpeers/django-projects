from django.urls import path
from .views import *


urlpatterns = [
    path("", GeeksCreate.as_view()),

]