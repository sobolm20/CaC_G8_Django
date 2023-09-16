from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "core/index.html", name=index)

def contact(request):
    return render(request, "core/contact.html", name=contact)

def details(request):
    return render(request, "core/details.html", name=details)


    