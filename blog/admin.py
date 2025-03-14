from django.contrib import admin
from .models import Blogger, Post, Comment

# Register
admin.site.register(Blogger)
admin.site.register(Post)
admin.site.register(Comment)
