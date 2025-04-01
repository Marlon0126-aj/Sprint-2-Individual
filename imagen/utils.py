from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def optimizar_imagen(imagen, calidad=70):
    img = Image.open(imagen)
    img = img.convert("RGB")
    
    output = BytesIO()
    img.save(output, format="JPEG", quality=calidad)
    output.seek(0)

    return ContentFile(output.read(), name=imagen.name)
