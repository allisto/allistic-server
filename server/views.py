from django.shortcuts import render

from .models import Parent


def index(request):
    parents = Parent.objects.all()
    args = {'parents': parents}
    return render(request, "server/index.html", args)


def patient(request):
    return render(request, "server/patient_page.html")
