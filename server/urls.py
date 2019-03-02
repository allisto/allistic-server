from django.urls import path

from server import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('patient/', views.patient, name="patient"),
]
