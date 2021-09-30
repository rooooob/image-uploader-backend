from django.urls import path
from . import views

app_name = 'imgapp'

urlpatterns = [
    path('images/', views.image_list, name='images-list'),
    path('images/<int:pk>/', views.image_detail, name='image-detail'),
    path('images/create/', views.image_create, name='image-create'),
    path('images/delete/<int:pk>/', views.image_delete, name='image-delete'),
]