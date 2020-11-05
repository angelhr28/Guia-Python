from PIL import Image
import math
ancho,alto = 0,0
def filtrar3x3(img,M):
    Ma,Mb,Mc = M[0][0],M[0][1],M[0][2]
    Md,Me,Mf = M[1][0],M[1][1],M[1][2]
    Mg,Mh,Mi = M[2][0],M[2][1],M[2][2]
    salida = Image.new("L",(ancho,alto))
    for i in range(1,img.size[0]-1): #empieza de 1 porque empieza desde el eje central y se resta -1 para que no tome img que no existe (ultimo pxel central)
        for j in range(2,img.size[1]-1): #float para para que me de decimal y pueda multiplicar con los filtros 
            Ia,Ib,Ic = float(img.getpixel((i-1,j-1))),float(img.getpixel((i-1,j))),float(img.getpixel((i-1,j+1))),
            Id,Ie,If = float(img.getpixel((i,j-1))),float(img.getpixel((i,j))),float(img.getpixel((i,j+1))),
            Ig,Ih,Ii = float(img.getpixel((i+1,j-1))),float(img.getpixel((i+1,j))),float(img.getpixel((i+1,j+1))),
            q = int(Ia*Ma+Ib*Mb+Ic*Mc+Id*Md+Ie*Me+If*Mf+Ig*Mg+Ih*Mh+Ii*Mi) #el valor de los pixeles es entero, por eso int
            salida.putpixel((i,j),q)
    return salida

imgGray = Image.open("paisaje.jpg").convert("L")
imgGray.show()
ancho,alto = imgGray.size
promedio = [[1/9,1/9,1/9],
            [1/9,1/9,1/9],
            [1/9,1/9,1/9]
            ]
gaussiano = [[1/16,2/16,1/16],
            [2/16,4/16,2/16],
            [1/16,2/16,1/16]
            ]
salida = filtrar3x3(imgGray,gaussiano)#promedio
salida.save("gaussiano.tif")
salida.show()
