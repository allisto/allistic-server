from django.shortcuts import render


def index(request):
    return render(request, "server/index.html")


def patient(request):
    return render(request, "server/patient_page.html")
