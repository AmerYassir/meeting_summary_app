from django.urls import path
from .views import upload_text

urlpatterns = [
    path('upload/', upload_text, name='upload_text'),
]