from django.urls import path
from .views import BlogList,BlogDetail,RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns=[path('blogs/',BlogList.as_view()),path('blogs/<int:pk>/',BlogDetail.as_view()),path('register/',RegisterView.as_view()),path('login/',TokenObtainPairView.as_view())]
