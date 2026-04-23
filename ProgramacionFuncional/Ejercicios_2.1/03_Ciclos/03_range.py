#Alan Alberto Colli Ake 8-B
from os import system
if system("clear") != 0: system("cls")

##range##
print("\nrange();")

print("generado de secuencia de numeros del 0 al 9")
for num in range(5, 10):
    print(num)

print("\n")

print("range(inicio, fin, paso")
for num in range(0, 1000, 5):
    print(num)

for num in range(-5, 0):
    print(num)

for num in range(0, 444):
    print(num)


nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

print("\n")

print("Seria para hacerlo cinco veces")
for _ in range(5):
    print("hacer cinco veces algo")

