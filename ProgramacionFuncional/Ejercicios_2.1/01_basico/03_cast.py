#Alan Alberto Colli Ake 8-B
##
#03_casting de types
#Trasformar un tipo de valor a otro
##

from os import system
if system("clear") !=0: system("cls")

print("Conversion de tipos")

#convertir una cadena que contiene un numero a entero y sumarlo con otro entero
print(int("100")+2)#Convierte 100 a entero y suma2.resultado 102

#convertir un entero a cadena para concatenarlo con otra cadena
print("100" + str(2))

#convertir una cadena con un numero decimal a tipo float
print(type(float("3.1416")))

#convertir un numero decimal a entero (se trunca la parte decimal)
print(int(3.1416))#convierte a 1.1416 a 3 eliminando los decimal

#Evaluar valores numericos como booleanos
print(bool(3))#cualquiero numeros distinto de 0 es True
print(bool(0))#0 es false resultado = false
print(bool(-1))#numeros negativos tambien son True 

#Evaluar cadenas como boleanos
print(bool(""))#Una cadena Vacia es false
print(bool(" "))#Una cadena con espacios es True
print(bool("False"))#Una cadena con texto, aunque sea False, es True 

#redondear un numero decimal
print(round(2.51))#Redondea 2.51 al entero mas cercano

#Este genera un error y ase comenta para evitar  conflicto en la ejecucion
#print(int("Hola Mundo"))