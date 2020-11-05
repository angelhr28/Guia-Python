from PIL import Image

ancho, alto = 0,0
def umbral2(img, u1,u2):
    salida = Image.new("L",(ancho, alto))
    for i in range (img.size[0]):
        for j in range (img.size[1]):
            p = img.getpixel((i,j))
            q = 0
            if p > u1 and p<u2:
                q = 255
            salida.putpixel((i,j),q)
    return salida

imgGray = Image.open("images.jpg").convert("L")
ancho, alto = imgGray.size
salida = umbral2(imgGray, 100,150)
salida.show()
