from django.shortcuts import render, HttpResponse

# Vista página home
def home(request):
    return render(request, "core/home.html")

# Vista página negocios
def negocios(request):
    return render(request, "core/negocios.html")

# Vista página Acerca del Club
def elclub(request):
    return render(request, "core/elclub.html")

# Vista página Contacto
def contacto(request):
    return render(request, "core/contacto.html")