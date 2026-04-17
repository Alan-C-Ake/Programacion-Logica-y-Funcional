#Alan Alberto Colli Ake 8-B
from os import system
if system("clear") != 0: system("cls")
###
# EJERCICIOS (while)
###

print("Ejercicio 1: Cuenta atrás")
# Imprime los números del 10 al 1 usando un bucle while.
contador = 10 
while contador >= 1:
    print(contador)
    contador -= 1

print("Ejercicio 2: Suma de números pares (while)")
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
contador = 2
suma = 0 
while contador <= 20:
    suma += contador
    contador += 2
print(f"La suma de los numeros pares es:{suma}")

print("Ejercicio 3: Factorial de un número")
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. 
# Por ejemplo, el factorial de 5 -> 5! = 5 x 4 x 3 x 2 x 1 = 120.

numero = -1
while numero < 0:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero < 0:
            print("Error: El número no puede ser negativo.")
    except ValueError:
        print("Error: Por favor, introduce un número válido.")

factorial = 1
contador = 1

while contador <= numero:
    factorial *= contador  
    contador += 1         

print(f"El factorial de {numero} es {factorial}")

print("Ejercicio 4: Validación de contraseña")
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

password = ""
while len(password) < 8:
    password = input("Introduce una contraseña (mínimo 8 caracteres): ")
    if len(password) < 8:
        print(f"Contraseña demasiado corta. Faltan caracteres.")

print("Contraseña válida")

print("Ejercicio 5: Tabla de multiplicar")
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

while True:
    try:
        num_tabla = int(input("¿Del 1 al 10 de cual número quieres la tabla?: "))
        
        i = 1
        while i <= 10:
            print(f"{num_tabla} x {i} = {num_tabla * i}")
            i += 1
        break 
    except ValueError:
        print("Error: ¡Debes introducir un número entero!")

print("Ejercicio 6: Números primos hasta N")
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

while True:
    try:
        n = int(input("Introduce un número entero positivo N: "))
        if n > 0:
            break
        print("Debe ser mayor a 0.")
    except ValueError:
        print("¡Error! Introduce un número entero.")

num = 2
while num <= n:
    divisores = 0
    i = 1
    
    while i <= num:
        if num % i == 0:
            divisores += 1
        i += 1
    
    if divisores == 2:
        print(num, end=" ")
        
    num += 1



###
# EJERCICIOS (for)
###

print("Ejercicio 1: Imprimir números pares")
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
for num in range(2, 21, 2):
    print(num, end=" ")
print()

print("Ejercicio 2: Calcular la media de una lista")
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
numeros = [10, 20, 30, 40, 50]
suma = 0

for n in numeros:
    suma += n

media = suma / len(numeros)
print(f"La media es: {media}")

print("Ejercicio 3: Buscar el máximo de una lista")
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]

for n in numeros:
    if n > maximo:
        maximo = n

print(f"El número máximo es: {maximo}")

print("Ejercicio 4: Filtrar cadenas por longitud")
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4: Filtrar cadenas por longitud")
palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

palabras_largas_for = [] 

for p in palabras:
    if len(p) > 5:
        palabras_largas_for.append(p)

print(f"Las palabras con mas de 5 letras son:  {palabras_largas_for}")

palabras_largas_comp = [p for p in palabras if len(p) > 5]

print(f"Las palabras con mas de 5 letras son: {palabras_largas_comp}")

print("Ejercicio 5: Contar palabras que empiezan con una letra")
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

letra = input("Introduce una letra para buscar: ")
contador = 0
for p in palabras:
    if p.lower().startswith(letra.lower()):
        contador += 1

print(f"Hay {contador} palabras que empiezan con la letra '{letra}'")