from django.urls import path
from .views import JobListView, RegisterView, LoginView

urlpatterns = [
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
