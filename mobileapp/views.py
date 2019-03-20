from django.shortcuts import render


def mobile(request):
    return render(request, "mobileapp/index.html")
