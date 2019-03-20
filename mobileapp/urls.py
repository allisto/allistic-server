from django.urls import path

from mobileapp import views

urlpatterns = [
    path('mobile/', views.mobile, name="index"),
]
