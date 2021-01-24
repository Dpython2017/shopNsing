from django.urls import path
from .api import UserCategory

urlpatterns = [
    path('category', UserCategory.as_view()),
]
