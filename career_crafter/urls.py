from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobportal.urls')),  # Replace 'your_app' with 'jobportal' or your actual app name
]
