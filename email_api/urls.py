
from django.urls import path, include
from .views import (
    EmaiApi,
)

urlpatterns = [
    path('send', EmaiApi.as_view()),
]