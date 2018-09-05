# -*- coding: utf-8 -*-
'''
Cruz Santos Isaac
Computación Gráfica
Grupo 04
'''

'''
Función de el algoritmo de LiangBarsky Visto en clase
modo == True -> Limites horizontales
modo = False -> Limites Verticales
vertices[0] = pxInf
vertices[1] = pyInf
vertices[2] = pxSup
vertices[3] = pySup
'''
import sys

def LiangBarsky(pRef, vertices, modo):
    u = 0
    try:
        # Modo horizontal
        if (modo):
            u = (pRef - vertices[0]) / (vertices[2] - vertices[0])
            if (u < 0 or u > 1):
                return False
            y = vertices[1] + u * (vertices[3] - vertices[1])
            punto = [pRef, round(y, 2)]

            if(validacion(punto)):
                return punto
            else:
                return False
        # Modo Vetical
        elif (modo is False):
            u = (pRef - vertices[1]) / (vertices[3] - vertices[1])
            if (u < 0 or u > 1):
                return False
            x = vertices[0] + u * (vertices[2] - vertices[0])
            punto = [round(x, 2), pRef]
            if(validacion(punto)):
                return punto
            else:
                return False
    except BaseException:
        return False

# Validacion del punto


def validacion(punto):

    if ((punto[0] >= verticeInf[0] and punto[0] <= verticeSup[0]) and (
            punto[1] >= verticeInf[1] and punto[1] <= verticeSup[1])):
        return True
    else:
        return False
# Impresión de puntos validos


def impPuntos(limite, punto):
    print(f"\tCon limite {limite}: ", end='')
    if(punto):
        print(f"Punto de recorte en: {punto} ")
    else:
        print("No tiene punto de recorte")


# Tomando entradas de ventana
verticeInf = []
verticeSup = []

while True:
    try:
        verticeInf = input(
            "Introduce las coordenadas del vertice inferior izquierdo: ").split(",")
        verticeInf = list(map(int, verticeInf))

        if(len(verticeInf) != 2):
            raise ValueError

    except BaseException:
        print("\n**Porfavor introduce las coordenadas separadas por comas, ejemplo 1,1. Asegurate que sean dos y que sean numeros enteros.\n")
        continue

    break

while True:
    try:
        size = input(
            "Introduce el ancho y alto de la ventana separado por comas: ").split(",")
        size = list(map(int, size))

        if(len(size) != 2):
            raise ValueError

    except BaseException:
        print("\n**Porfavor introduce el ancho y alto separado por comas, ejemplo 300,200. Asegurate que sean dos valores y que sean numeros enteros.\n")
        continue

    verticeSup = [verticeInf[0] + size[0], verticeInf[1] + size[1]]

    break

# Imprimiendo Datos de ventana
print("\nDatos de Ventana: ")
print(f"Tamaño de ventana: {size[0]} x {size[1]}")
print("Vertice inferior izquierdo: ", verticeInf)
print("Vertice superior derecho: ", verticeSup)

# Abriendo el archivo en modo lectura
try:
    archivo = open("lineas.txt", "r")
#Si no se puede abrir terminamos ejecución
except:
    print("\n***No se ha podido abrir el archivo 'lineas.txt'***")
    sys.exit(1)

archivo_leido = archivo.read().split("\n")
archivo.close()

# Casteando datos a enteros
lineas = []
for linea_s in archivo_leido:
    linea_i = linea_s.split(" ")
    lineas.append(list(map(int, linea_i)))

# Imprimiendo puntos de recorte
for indice, linea in enumerate(lineas, start=1):

    print(f"\nPara la linea {indice}:")

    pIzq = LiangBarsky(verticeInf[0], linea, True)
    impPuntos("izquierdo", pIzq)

    pDer = LiangBarsky(verticeSup[0], linea, True)
    impPuntos("derecho", pDer)

    pInf = LiangBarsky(verticeInf[1], linea, False)
    impPuntos("inferior", pInf)

    pSup = LiangBarsky(verticeSup[1], linea, False)
    impPuntos("superior", pSup)
