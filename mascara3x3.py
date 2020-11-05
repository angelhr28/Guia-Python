from PIL import Image

ancho, alto = 0,0

def filtrar3x3(img,masc):
    mascA,mascB,mascC = masc[0][0],masc[0][1],masc[0][2]
    mascD,mascE,mascF = masc[1][0],masc[1][1],masc[1][2]
    mascG,mascH,mascI = masc[2][0],masc[2][1],masc[2][2]
    salida = Image.new("L",(ancho,alto))
    for i in range(1,img.size[0]-1):
        for j in range(1,img.size[1]-1):
            Ia, Ib, Ic = float (img.getpixel((i-1,j-1))),float (img.getpixel((i-1,j))),float (img.getpixel((i-1,j+1)))
            Id, Ie, If = float (img.getpixel((i,j-1))),float (img.getpixel((i,j))),float (img.getpixel((i,j11)))
            Ig, Ih, Ii = float (img.getpixel((i+1,j-1))),float (img.getpixel((i+1,j))),float (img.getpixel((i+1,j+1)))
            q = int(Ia*mascA + Ib*mascB + Ic*mascC + Id*mascD + Ie*mascE + If*mascF + Ig*mascG + Ih*mascH + Ii*mascI )
            salida.putpixel()
            
    
promedio = [[1/9,1/9,1/9],
            [1/9,1/9,1/9],
            [1/9,1/9,1/9]]
imgGray = Image.open("images.jpg").convert("L")
salida.show()
ancho, alto = imgGray.size
salida = filtrar3x3(img,promedio)
salida.show()
