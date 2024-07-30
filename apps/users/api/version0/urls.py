from django.urls import path

from .views import user_create, user_update, user_delete

app_name = 'user_api'

urlpatterns = [
    path('create/', user_create, name='user_create'),
    path('update/<int:pk>', user_update, name='user_update'),
    path('delete/<int:pk>', user_delete, name='user_delete'),
]
