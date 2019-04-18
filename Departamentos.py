'''
Created on 17-04-2019
#Programa que permite revisar el precio de departamentos con diferentes precios
@author: Vicente Bustamante P; Ejercicio No. 2
'''
#Ciclo que permite validar el rango de los deapartamentos
repite = True
while repite:
    Dep = str(input("Ingrese el departamento para consultar su valor: "))
    Depto = int(Dep)
    if (Depto < 101) or (Depto > 2008):
        print("Error departamento inexistente")
    else:
        repite = False
largo = (len(Dep))
ultimo = Dep[largo - 1:]
nu = int(ultimo)
valor = 0
piso = ""
#Preguntas para idantificar el valor del departamento
if (Depto > 200) and (Depto < 1909):
    valor = 250
    piso = "entremedio"
if (Depto > 100) and (Depto < 109):
    valor = 100
    piso = "primero"
if (Depto > 2000) and (Depto < 2009):
    valor = 400
    piso = "ultimo"
#Se aplica porcentaje a los departamentos de los costados
if (nu == 7) or (nu == 8):
    valor = (valor * 1.15)
if (nu == 1) or (nu == 2):
    valor = valor - ((valor * 20) / 100)
print("El valor del departamento del piso" , piso , "es: " , round(valor,2))    
