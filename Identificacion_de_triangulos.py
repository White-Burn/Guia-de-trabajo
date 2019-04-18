'''
Created on 17-04-2019
#Este programa permite identificar los tipos de triangulo
@author: Vicente Bustamante P; Ejercicio No. 3
'''
angu1 = int(input("Ingrese el primer angulo: "))
angu2 = int(input("Ingrese el segundo angulo: "))
angu3 = (angu1 + angu2)
angu_f = (180 - angu3)
#Se pregunta por cada condicion de tipo de angulo
if (angu_f) == 90:
    print("El triangulo es rectangulo. ")
else:
    if (angu1 < 90) and (angu2 < 90) and (angu_f < 90):
        print("El triangulo es acutangulo. ")
    else:
        if (angu1 > 90) or (angu2 > 90) or (angu_f > 90):
            print("El traingulo es obtusangulo. ")