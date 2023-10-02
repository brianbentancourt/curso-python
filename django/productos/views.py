from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
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


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    return render(
        request,
        'detalle.html',
        context={'producto': producto}
    )
