from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.

# /productos


def index(request):
    productos = Producto.objects.all()
    # productos = Producto.objects.filter(puntaje__gte=3)
    # productos = Producto.objects.get(id=1)

    return render(
        request,
        'index.html',
        context={'productos': productos}
    )
