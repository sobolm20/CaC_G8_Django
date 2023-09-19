from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def details(request):
    return render(request, "details.html")

def year_archive(request, year):
    response = HttpResponse(f"Archivos el año {year}")
    if year == 2023:
        url = reverse("index")
        response = HttpResponseRedirect(url)
    elif year == 2029:
        response = HttpResponseServerError("CUalquier cosa")

    return response
    