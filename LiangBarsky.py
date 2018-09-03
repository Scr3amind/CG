# -*- coding: utf-8 -*-
verticeInf = []
verticeSup = []


#Función de el algoritmo de LiangBarsky Visto en clase
#modo == True -> Limites horizontales
#modo = False -> Limites Verticales
#vertices[0] = pxInf
#vertices[1] = pyInf
#vertices[2] = pxSup
#vertices[3] = pySup
def LiangBarsky(pRef,vertices,modo): 
    u = 0
    try:
        if (modo == True):
            u = (pRef - vertices[0]) / (vertices[2] - vertices[0])
            if (u < 0 or u > 1):
                return False
            y = vertices[1] + u * (vertices[3] - vertices[1])
            punto = [pRef , y]
            return punto
        
        elif (modo == False):
            u = (pRef - vertices[1]) / (vertices[3] - vertices[1])
            if (u < 0 or u > 1):
                return False
            x = vertices[0] + u * (vertices[2] - vertices[0])
            punto = [x , pRef]
            return punto
    except:
        return False


def validacion(punto):
    
    if(punto==False):
        return False
    if ((punto[0] >= verticeInf[0] and punto[0] <= verticeSup[0]) and (punto[1] >= verticeInf[1] and punto[1] <= verticeSup[1])):
        return True
    else:
        return False


    



while True:
    try:
        verticeInf = input("Introduce las coordenadas del vertice inferior izquierdo: ").split(",")
        verticeInf = list(map(int,verticeInf))
        
        if(len(verticeInf)!=2):
            raise ValueError
    
    except:
        print("\n**Porfavor introduce las coordenadas separadas por comas, ejemplo 1,1. Asegurate que sean dos y que sean numeros enteros.\n")
        continue
    print(verticeInf)
    break

while True:
    try:
        size = input("Introduce el ancho y alto de la ventana separado por comas: ").split(",")
        size = list(map(int,size))

        if(len(size)!=2):
            raise ValueError
    
    except:
        print("\n**Porfavor introduce el ancho y alto separado por comas, ejemplo 300,200. Asegurate que sean dos valores y que sean numeros enteros.\n")
        continue

    verticeSup =[verticeInf[0]+size[0],verticeInf[1]+size[1]]
    
    print(size)
    print(verticeSup)
    break


archivo = open("lineas.txt","r")
archivo_leido = archivo.read().split("\n")
archivo.close()
print(archivo_leido)
lineas = []
for linea_s in archivo_leido:
    linea_i=linea_s.split(" ")
    lineas.append(list(map(int,linea_i)))
i=1
for linea in lineas:
    
    print(f"Linea {i}")
    print(LiangBarsky(verticeInf[0],linea,True))
    print(LiangBarsky(verticeSup[0],linea,True))
    print(LiangBarsky(verticeInf[1],linea,False))
    print(LiangBarsky(verticeSup[1],linea,False))
    i=i+1
    
