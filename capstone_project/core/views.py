from django.shortcuts import render, HttpResponse

# Vista página home
def home(request):
    return render(request, "core/home.html")

# Vista página negocios
def negocios(request):
    return render(request, "core/negocios.html")