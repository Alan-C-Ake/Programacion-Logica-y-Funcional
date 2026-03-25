#Alan Alberto Colli Ake
#Entrada de usuario
from os import system
if system("clear") !=0: system("cls")

#obtencion de datos del usuario se usa input()
nombre = input("Hola, como te llamas")
print(f"Hola {nombre}, encantada de concerte")

age = input("Cuantos años tienes?\n")
age = int(age)
print(f"tienes {age}, años")


print("Obtener multiples valores a la vez")
country, city =input("En que pasis y ciudad vives?\n").split()

print(f"vives en {country}, {city}")