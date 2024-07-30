from django.urls import path

from apps.follower.api.version0.views import follower_create, following_create

urlpatterns = [
    path('following/', following_create, name='following_create'),
    # path('following-list/', following_list, name='following_list'),
    # path('follower-list/', follower_list, name='follower_list'),
]
