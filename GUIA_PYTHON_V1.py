#SESION 1 DE SISTEMAS INTELIGENTES

#DECLARAR UNA LIBRERIA
from PIL import Image

#PARA INSTALAR UNA LIBRERIA SE DEBE COLOCAR EL SIGUIENTE TEXTO
#    pip install <LIBRERIA>

#LENGUAJE NO TIPADO

#DECLARACION DE VARIABLES
y="Hola"
x=10
print(y,"mundo cruel")

#CONDUCIONALES O FUNCIONES SE INICIAN CON : EN VEZ DE {}
#SE BASA EN LA IDENTACION
if x>0:
    print("positivo")
    print("Ultrapositivo")
else:
    if x<0:
        print("negativo")
        print("ultranegativo")
    else:
        print("Cero")
print("resuelto")

#DECLARACION DE UN ARREGLO 
mascotas=["gato","perro","loro","guepardo"]

#BUCLE FOR BY INDEX
for i in range(len(mascotas)):
    print(mascotas[i])

#BUCLE FOR BY ELEMTO
for m in mascotas:
    print(m)

#DECLARACION DE ARREGLO BY BUCLE     
numeros = [i for i in range(5)]
print(numeros)

#DECLARACION DE ARREGLO CONCATENADO BY BUCLE     
rangos = ["rango " + str(i+1) for i in range(5)]
print(rangos)

#FUNCIONES
def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b               

#CAPTURA DE VALORES POR TECLADO 
a=int(input("ingresar a: "))
b=int(input("ingresar b: "))

s=sumar(a,b)
r=restar(a,b)

print("la suma es: ",s)
print("la resta es: ",r)

#AGREGAR ELEMENTOS A UN ARREGLO DEFINIDO
mascotas.append("iguana")

#RETIRAR ELEMENTOS A UN ARREGLO DEFINIDO
mascotas.pop(0)
print(mascotas)

#DELCARACION MULTIPLE DE VARIABLES
x,y,z = 10,20,30
print(x,y,z)

#NUMERO MAYOR A MENOR 
def numMayor(a,b,c):
    numbers = []
    numbers.append(a)
    numbers.append(b)
    numbers.append(c)
    numeros = [i for i in sorted(numbers, reverse=True)]
    print (numeros)

a=int(input("ingresar a: "))
b=int(input("ingresar b: "))
c=int(input("ingresar c: "))
numMayor(a,b,c)





