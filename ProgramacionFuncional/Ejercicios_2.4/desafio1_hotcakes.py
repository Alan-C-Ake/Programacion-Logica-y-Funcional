#desafio 1: Ordenar hotcakes para la famlilia
#objetivo: crear un programa que simule la prepación de piezas de hotkakes  y ordenar de acuerdo al numero de integrantes de mi familia


'''
define una funcion que no reciba parametros y devuelva el emoji de hotcake.
esta funcion simulara la prepacion de una pieza de hotcake.

crea una segunda funcion que reciba un argumento numero_piezas, rewpresentando la cantidad de piezas de hotcake a preparar 
 Dentro de la funcion
- Almacena los resultados en una lista llamada piezas_hotcakes
- Usa una compresion de listas para llamar a la funcion preparar_hotcake tantas veces como el numero indicado en numero_piezas
- Devuelve la lista piezas_hotcake 

llama a la segunda funcion solicitando al usuario ingresar el numero de integrantes en su familia y almacena el resultado en una 
variable hotcake_familia

muestra en pantalla el contenido de la variable hotcake_familia, que sera una lista con varias emojis"🥞"
'''

def preparar_hotcake():
    return "🥞"   

def ordenar_hotcake(numero_piezas):
    piezas_hotcake = [preparar_hotcake() for _ in range(numero_piezas)]
    return piezas_hotcake

hotcake_familia  = ordenar_hotcake(int(input("Ingrese el numero de hotcakes de acuerdo a la familia: ")))
print(hotcake_familia)