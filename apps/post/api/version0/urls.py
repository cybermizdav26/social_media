from django.urls import path

from .views import (
    post_create,
    post_update,
    post_list,
    like_post,
    comment_create,
    comment_list,
    post_delete,
    comment_delete
)

app_name = 'api_post'

urlpatterns = [
    path('post-create/', post_create, name='post_create'),
    path('post-list/', post_list, name='post_list'),
    path('post-update/<str:id>', post_update, name='post_update'),
    path('post-delete/<str:id>', post_delete, name='post_delete'),
    path('post-like/', like_post, name='liked_post'),
    path('comment-create/', comment_create, name='comment_create'),
    path('comment-list/', comment_list, name='comment_list'),
    path('comment-delete/<str:id>', comment_delete, name='comment_delete')
]
