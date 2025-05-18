from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY='your-secret'
DEBUG=True
ALLOWED_HOSTS=['*']
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','rest_framework','blog']
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR / 'db.sqlite3',}}
REST_FRAMEWORK={'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework_simplejwt.authentication.JWTAuthentication'],'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination','PAGE_SIZE':5}
ROOT_URLCONF='blog_backend.urls'
