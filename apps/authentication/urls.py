from django.urls import path

from apps.authentication.api.viewsets import RegisterView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
