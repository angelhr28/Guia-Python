from PIL import Image
import math
ancho,alto = 0,0
def resalteborde(img,H,V):
    Ha,Hb,Hc = H[0][0],H[0][1],H[0][2]
    Hd,He,Hf = H[1][0],H[1][1],H[1][2]
    Hg,Hh,Hi = H[2][0],H[2][1],H[2][2]

    Va,Vb,Vc = V[0][0],V[0][1],V[0][2]
    Vd,Ve,Vf = V[1][0],V[1][1],V[1][2]
    Vg,Vh,Vi = V[2][0],V[2][1],V[2][2]
    salida = Image.new("L",(ancho,alto))
    for i in range(2,img.size[0]-1):
        for j in range(2,img.size[1]-1):
            Ia,Ib,Ic = float(img.getpixel((i-1,j-1))),float(img.getpixel((i-1,j))),float(img.getpixel((i-1,j+1))),
            Id,Ie,If = float(img.getpixel((i,j-1))),float(img.getpixel((i,j))),float(img.getpixel((i,j+1))),
            Ig,Ih,Ii = float(img.getpixel((i+1,j-1))),float(img.getpixel((i+1,j))),float(img.getpixel((i+1,j+1))),
            Gx = Ia*Ha+Ib*Hb+Ic*Hc+Id*Hd+Ie*He+If*Hf+Ig*Hg+Ih*Hh+Ii*Hi
            Gy = Ia*Va+Ib*Vb+Ic*Vc+Id*Vd+Ie*Ve+If*Vf+Ig*Vg+Ih*Vh+Ii*Vi
            q = int(math.sqrt(Gx*Gx+Gy*Gy))
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


RobertsH = [[0.0,0.0,0.0],
            [0.0,1.0,0.0],
            [0.0,0.0,-1.0]
            ]
RobertsV = [[0.0,0.0,0.0],
            [0.0,0.0,1.0],
            [0.0,-1.0,0.0]
         ]

PrewitH = [[-1.0,0.0,1.0],
            [-1.0,0.0,1.0],
            [-1.0,0.0,1.0]
            ]
PrewitV = [[-1.0,-1.0,-1.0],
            [0.0,0.0,0.0],
            [1.0,1.0,1.0]
            ]

SobelH = [[1.0,0.0,-1.0],
            [2.0,0.0,-2.0],
            [1.0,0.0,-1.0]
            ]
SobelV = [[-1.0,-2.0,-1.0],
            [0.0,0.0,0.0],
            [1.0,0.0,1.0]
            ]
resultado = resalteborde(imgGray,SobelH,SobelV)
resultado.save("Sobel.tif")
resultado.show()
