from django.shortcuts import render
from .models import Kategori,Filmler


def home(request):
    data = {
        "kategoriler":Kategori.objects.all(),
        "filmler":Filmler.objects.filter(anasayfa=True)
    }
    return render(request, "home.html", data )

def movies(request):
    data = {
        "kategoriler":Kategori.objects.all(),
        "filmler":Filmler.objects.all()
    }
    return render(request, "movies.html", data )

def moviesdetails(request, id):
    data = {
        "film":Filmler.objects.get(id=id)
    }
    return render(request, "details.html", data )

def error(request):
    return render(request,"error.html")