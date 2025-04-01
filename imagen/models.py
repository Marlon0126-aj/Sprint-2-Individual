from django.db import models

class Imagen(models.Model):
    imagen_original = models.ImageField(upload_to="originales/")
    imagen_optimizada = models.ImageField(upload_to="optimizadas/", blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

