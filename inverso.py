from PIL import Image

ancho, alto = 0,0
def inverso(img):
    salida = Image.new("L",(ancho, alto))
    for i in range (img.size[0]):
        for j in range (img.size[1]):
            p = img.getpixel((i,j))
            q = 255 - p # inverso
            salida.putpixel((i,j),q)
    return salida

imgGray = Image.open("images.jpg").convert("L")
ancho, alto = imgGray.size
salida = inverso(imgGray)
salida.show()

