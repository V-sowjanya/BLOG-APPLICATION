from rest_framework import generics,permissions
from .models import Blog
from .serializers import BlogSerializer,UserSerializer
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.views import TokenObtainPairView
class RegisterView(generics.CreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=UserSerializer
class BlogList(generics.ListCreateAPIView):
    queryset=Blog.objects.all().order_by('-created_at')
    serializer_class=BlogSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_update(self,serializer):
        if self.request.user!=self.get_object().author:
            raise PermissionDenied()
        serializer.save()
    def perform_destroy(self,instance):
        if self.request.user!=instance.author:
            raise PermissionDenied()
        instance.delete()
