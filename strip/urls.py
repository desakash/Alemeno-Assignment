from django.urls import path
from .views import upload_image,index

urlpatterns = [
    path('strip/upload/', upload_image, name='upload_image'),
    path('', index, name='index'),  
]