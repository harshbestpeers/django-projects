from django.contrib import admin
from .models import Board,Post,Topic

# Register your models here.



admin.site.register(Topic)
admin.site.register(Board)
admin.site.register(Post)
