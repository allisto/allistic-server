from django.shortcuts import render

from .models import Parent


def index(request):
    parents = Parent.objects.all()
    args = {'parents': parents}
    return render(request, "server/index.html", args)


def patient(request, post_id):
    parent = Parent.objects.get(id=post_id)
    args = {'parent': parent}
    return render(request, "server/patient_page.html", args)
