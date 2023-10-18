from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('threshold/', views.thresholdOp),
    path('colors/', views.color_range),
    path('streaming/', views.streaming_webcam),
    path('webcam_feed/',views.webcam_feed, name = 'webcam_feed'),
]