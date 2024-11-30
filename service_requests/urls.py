from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_request, name='create_request'),
    path('view/', views.view_requests, name='view_requests'),
    path('track/<int:request_id>/', views.track_request, name='track_request'),
]
