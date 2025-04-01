from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Imagen
from .utils import optimizar_imagen
from .forms import ImagenForm

def subir_imagen(request):
    if request.method == "POST":
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            imagen_obj = form.save(commit=False)
            imagen_obj.imagen_optimizada.save(
                imagen_obj.imagen_original.name,
                optimizar_imagen(imagen_obj.imagen_original)
            )
            imagen_obj.save()
            return redirect("imagen_exitosa")
    else:
        form = ImagenForm()
    
    return render(request, "imagen/subir_imagen.html", {"form": form})

def imagen_exitosa(request):
    return render(request, "imagen/imagen_exitosa.html")
