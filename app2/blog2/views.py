from django.shortcuts import render


# Create your views here.

def url(request):
    return render(request, "blog2/Hello.html")


def new_(request):
    return render(request, "blog2/new.html")


def iam(request):
    return render(request, "blog2/hi.html")
