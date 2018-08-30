
verticeInf = []
verticeSup = []


#Función de el algoritmo de LiangBarsky Visto en clase
#modo == True -> Limites horizontales
#modo = False -> Limites Verticales
def LiangBarsky(pRef,pxInf,pyInf,pxSup,pySup,modo): 
    u = 0
    if (modo == True):
        u = (pRef - pxInf) / (pxSup - pxInf)
        if (u < 0 or u > 1):
            return False
        y = pyInf + u * (pySup - pyInf)
        punto = [pRef , y]
        return punto
    
    elif (modo == False):
        u = (pRef - pyInf) / (pySup - pyInf)
        if (u < 0 or u > 1):
            return False
        x = pxInf + u * (pxSup - pxInf)
        punto = [x , pRef]
        return punto

def validacion(punto):
    
    if(punto==False):
        return False
    if ((punto[0] >= verticeInf[0] and punto[0] <= verticeSup[0]) and (punto[1] >= verticeInf[1] and punto[1] <= verticeSup[1])):
        return True
    else:
        return False


    



while True:
    verticeInf = input("Introduce las coordenadas del vertice inferior izquierdo: ").split(",")
    verticeInf = list(map(int,verticeInf))
    
    if(len(verticeInf)!=2):
        print("**Porfavor introduce las coordenadas separadas por comas, ejemplo 1,1. Asegurate que sean dos y que sean numeros enteros.")
        continue
    
    print(verticeInf)
    break

while True:
    size = input("Introduce el ancho y alto de la ventana separado por comas: ").split(",")
    size = list(map(int,size))

    if(len(size)!=2):
        print("**Porfavor introduce el ancho y alto separado por comas, ejemplo 300,200. Asegurate que sean dos valores y que sean numeros enteros.")
        continue

    verticeSup =[verticeInf[0]+size[0],verticeInf[1]+size[1]]
    
    print(size)
    print(verticeSup)
    break


archivo = open("lineas.txt","r")
archivo_leido = archivo.read().split("\n")
print(archivo_leido)
lineas = []
for linea_s in archivo_leido:
    linea_i=linea_s.split(" ")
    lineas.append(list(map(int,linea_i)))

for linea in lineas:
    print(LiangBarsky(verticeInf[0],linea[0],linea[1],linea[2],linea[3],True))
    print(LiangBarsky(verticeSup[0],linea[0],linea[1],linea[2],linea[3],True))
    print(LiangBarsky(verticeInf[1],linea[0],linea[1],linea[2],linea[3],False))
    print(LiangBarsky(verticeSup[1],linea[0],linea[1],linea[2],linea[3],False))

    