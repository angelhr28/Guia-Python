from PIL import Image

ancho, alto = 0,0
def umbral1(img, u):
    salida = Image.new("L",(ancho, alto))
    for i in range (img.size[0]):
        for j in range (img.size[1]):
            p = img.getpixel((i,j))
            q = 0
            if p > u:
                q = 255
            salida.putpixel((i,j),q)
    return salida

imgGray = Image.open("images.jpg").convert("L")
ancho, alto = imgGray.size
salida = umbral1(imgGray, 128)
salida.show()
