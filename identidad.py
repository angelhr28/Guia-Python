from PIL import Image

ancho, alto = 0,0
def identidad(img):
    salida = Image.new("L",(ancho, alto))
    for i in range (img.size[0]):
        for j in range (img.size[1]):
            p = img.getpixel((i,j))
            q = p # identidad
            salida.putpixel((i,j),q)
    return salida

imgGray = Image.open("images.jpg").convert("L")
ancho, alto = imgGray.size
salida = identidad(imgGray)
salida.show()

