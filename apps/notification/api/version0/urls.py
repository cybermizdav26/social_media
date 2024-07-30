from django.urls import path

from apps.notification.api.version0.views import notification_list, notification_retrieve

urlpatterns = [
    path("", notification_list, name="notification-list"),
    path("<int:pk>", notification_retrieve, name="notification-retrieve"),
]