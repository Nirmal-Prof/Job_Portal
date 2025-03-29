from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Job, JobApplication
from .serializers import RegisterSerializer, LoginSerializer, JobSerializer, JobApplicationSerializer
from .permissions import IsEmployer, IsJobSeeker

# User Registration
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# User Login
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

# Post Job (Employer Only)
class PostJobView(generics.CreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmployer]

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)

# List Jobs
class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# Apply for Job (Job Seeker Only)
class ApplyJobView(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsJobSeeker]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
