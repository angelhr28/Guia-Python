from PIL import Image
ancho,alto = 0,0 
def identidad(img):
    salida = Image.new("L",(ancho,alto)) #crea la imagen final
    for i in range(img.size[0]): #recorrer la dimension m
        for j in range(img.size[1]): #recorrer la dimension n
            p = img.getpixel((i,j)) #(i,j) es un parametro de entrada
            q = p # identidad
            salida.putpixel((i,j),q) #asignar a salida
    return salida

def inverso(img):
    salida = Image.new("L",(ancho,alto))
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            p = img.getpixel((i,j))
            q = 255- p # inverso
            salida.putpixel((i,j),q)
    return salida
def umbral1(img,u):
    salida = Image.new("L",(ancho,alto))
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            p = img.getpixel((i,j))
            if p>u:
                q = 255
            else:
                q = 0
            salida.putpixel((i,j),q)
    return salida

def umbral1inverso(img,u):
    salida = Image.new("L",(ancho,alto))
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            p = img.getpixel((i,j))
            if p>u:
                q = 0
            else:
                q = 255
            salida.putpixel((i,j),q)
    return salida

def umbral2(img,u1,u2):
    salida = Image.new("L",(ancho,alto))
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            p = img.getpixel((i,j))
            if p>=u1 and p>=u2:
                q = 255
            else:
                q = 0
            salida.putpixel((i,j),q)
    return salida

def umbral2inverso(img,u1,u2):
    salida = Image.new("L",(ancho,alto))
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            p = img.getpixel((i,j))
            if p>=u1 and p>=u2:
                q = 0
            else:
                q = 255
            salida.putpixel((i,j),q)
    return salida

imgGray = Image.open("paisaje.jpg").convert("L") #CONVERTIR A TONO DE GRIS
imgGray.show() 
ancho,alto = imgGray.size #DEVUELVE EL mxn
salida = umbral2inverso(imgGray,100,100) #umbral2(imgGray,100,100)#umbral1inverso(imgGray,128)#umbral1(imgGray,128)#inverso(imgGray)#identidad(imgGray)
salida.save("umbral1.tif")
salida.show()
