#Alan Alberto Colli Ake

from os import system
if system("clear") !=0: system("cls")

#Las variables sirven para guardar datos en memoria

#para asignar una variable solo hace falta poner el nombre de la variable y asignarle un valor
my_name = "AlanColli"
print(my_name)#imprime valor de la variable my_name

age = 22
print(age)#ahora la variable age tiene el valor 22
#Reasigna valor
age = 22
print(age)#Ahora es 22

#Tipado dinamico: el tipo de determine en tiempo de ejecucion
#no es neceasrio declarar el tipo de datos

name = "AlanColli"
print(type(name))#ahora la variable tiene un numero entero int 

#tipado fuerte: phyton no realiza conversiones automaticas 
#Esto genera un error porque no se puede sumar un numero con una cadena 
#print(10+"2") 

#f-string(literal de cadena de formato)
print(f"Hola {my_name}, tengo {age+5} años")

#no recomendada forma de asignar varoiable
name, age, city = "AlanColli", 22, "FcP"

#conversionnes de nombres a variables
mi_nombre_de_variable = "ok" #snake case
nombre = "ok"

mi_nombre_de_variable = "no recomendado"#camelCase
mi_nombre_de_variable = "no recomendable"#pascalCase
mi_nombre_de_variable = "no recomendado"#todoJunto

mi_nombre_de_variable_123="ok"

MI_CONSTANTE = 3.1416 #UPERCASE CONSTANTE

#Anotaciones de tipo (opcional, para mayor claridad en el codigo)
is_user_logged_in : bool = True #indica que la variable es un booleano
print(is_user_logged_in)

