from django.contrib import admin

from .models import PostImage, Post, LikedPost, Comment, LikedComment

admin.site.register(PostImage)
admin.site.register(Post)
admin.site.register(LikedPost)
admin.site.register(Comment)
admin.site.register(LikedComment)
