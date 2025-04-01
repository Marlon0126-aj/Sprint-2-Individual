from django.urls import path
from .views import subir_imagen, imagen_exitosa

urlpatterns = [
    path("subir/", subir_imagen, name="subir_imagen"),
    path("exitosa/", imagen_exitosa, name="imagen_exitosa"),
]
