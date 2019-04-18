'''
Created on 17-04-2019
#Programa que permite ingresar una puntuacion de clavados y las calcula
@author: Vicente Bustamante P; Ejercicio No. 4
'''
Puntajes = []
nombre = str(input("Nombre de el clavadista: "))
gradoDif = float(input("Grado de dificultad: "))
#Ciclo for permite el ingreso de puntuacion optimizado
for x in range(1,8):
    #Ciclo while valida ingreso de el rango
    repite = True
    while repite:
        print("Ingrese la puntuacion del Juez",x,": ", end="")
        pun = float(input())
        if (pun < 1) or (pun > 10):
            print("Error la puntuacion es de 1 a 10")
        else:
            Puntajes.append(pun)
            repite = False
menor = 10
mayor = 1
suma = 0
#Ciclo para obtener el puntaje mayor y el menor
for ptje in Puntajes:
    suma = suma + ptje
    if (ptje > mayor):
        mayor = ptje
    if (ptje < menor):
        menor = ptje
#Calculo del puntaje total
ptjeTotal = suma - (mayor + menor)
p_f = (ptjeTotal * (3/5) * (gradoDif) )
print("La puntuacion final es: " , p_f)