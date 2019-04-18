'''
Created on 14-04-2019
#Programa que calcula el anio, mes y dia que naciste
@author: Vicente Bustamante P
'''
anio = int(input("Ingrese el anio en que nacio: "))
mes = int(input("Ingrese el mes en que nacio: "))
dia = int(input("Ingrese el dia en que nacio: "))
anioahora = (2019 - anio)
mesahora = 4 - mes
diaahora = 12 - dia 
if (diaahora < 0):
    mesahora = mesahora - 1
    diaahora = diaahora + 30
if (mesahora < 0):
    anioahora = anioahora - 1
    mesahora = mesahora + 12
print (str("Edad: ") ,(anioahora) ,"anios,", (mesahora), "meses, ", (diaahora), "dias")