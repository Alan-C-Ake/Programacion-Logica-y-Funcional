#Alan Alberto Colli Ake 8-B

from os import system
if system("clear") != 0: system("cls")


print("\n Bucle while")

contador = 0

while contador <= 5:
    print(contador)
    contador += 1

print("\n Bucle while con break")

contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

print("\n Bucle con continue")

contador = 0

while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue
    print(contador)

print("\n Bucle while con else")
contador = 0

while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")



numero = -1

while numero <0:
    numero = int(input("Escribe un numero positivo: "))
    if numero <0:
        print("El numero debe de ser positivo. intenta otra vez")

print(f"El numero que has ingresado es {numero}")


numero= -1
while numero < 0:
    try:
        numero = int(int(input("Escribe un numero positivo: ")))
        if numero <0:
         print("El numero debe ser positivo: ")
    except:
        print("lo que introduces debe de ser un numero!")

print(f"El numero que has introducido es {numero}")




