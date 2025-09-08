#Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

#Inicializamos la variable 'num' para que la tome a partir de cero 
num = 0

#Establecemos el bucle 'while' y las condiciones de la iteración para que se ejecute correctamente
while num <= 100:
    print (num)
    num = num + 1

#Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 

#Realizamos una presentación como título del programa
print("CONTADOR DE DÍGITOS DE NÚMEROS ENTEROS")

#Solicitud al usuario para que ingrese el número entero
numero = int(input("Ingrese un número entero: "))

#Pedimos a Python que tome el valor absoluto del número en caso de que el usuario ingrese un negativo
num = abs(numero)
#A su vez tomamos al cero como caso especial mediante una condicional 'if'
if num == 0:
    digitos = 1
else:
    digitos = 0   #Reiniciamos la variable para el resto de números
    while num > 0:
        num //=10 #Utilizamos este modo para que efectúe la división entera del número elegido y su reasignación para obtener la cantidad de digitos
        digitos += 1

#Cerramos el programa con la devolución por pantalla
print("El número", numero, "tiene", digitos, "dígitos.")

#Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

#Solicitamos los números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

#Mediante una condicional aseguramos que la variable 'num 2' aloje al mayor número, independientemente del orden de elección del usuario
if num1 > num2:
    num1, num2 = num2, num1

#Inicializamos la variable 'suma' y el iterador para que efectúe la suma exceptuando al valor menor
suma = 0
iter = num1 + 1

#Ejecutamos el bucle 'while' con las instrucciones para que efectúe la suma
while iter < num2: 
    suma += iter
    iter += 1

#Realizamos la salida con el resultado en pantalla
print(f"La suma de los números enteros comprendidos entre {num1} y {num2} es: {suma}")   

 #Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 
#Solicitamos al usuario que ingrese los números que desee sumar, inicializando la variable para alojarlos a medida que se reciben
print("Ingrese los números enteros que desee sumar (presione 0 para finalizar):")
numero = int(input("Número: "))

#Inicializamos la variable 'suma'
suma = 0

#Ejecutamos el bucle 'while' con las condiciones para que se efectúe la suma y se detenga al recibir un 0, haciendo que se mantenga mientras el usuario ingrese otros valores

while numero != 0:
    suma += numero
    numero = int(input("Número: "))

#Mostramos la salida por pantalla con el resultado de la suma
print(f"La suma de los números ingresados es: {suma}")

#Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

#Importamos la biblioteca 'random', necesaria para poder establecer un valor aleatorio
import random

#Mediante ella, incializamos la variable y solicitamos la generación de un número aleatorio que será el que se tenga que adivinar
aleatorio = random.randint(0, 9)

print("Adivina cuál es el número secreto")

#Inicializamos las variables para que el usuario ingrese el número y el contador de intentos
elegido = -1 #Utilizando un valor fuera de rango, evitamos que sea el aleatorio generado a adivinar
intentos = 0

#Mediante un bucle 'while' solicitamos el ingreso del número al usuario, a medida que se registran los intentos
while elegido != aleatorio:
    elegido = int(input("Ingresa el número de tu elección: "))
    intentos +1= 1

print(f"¡Felicidades! Has encontrado el número {aleatorio} luego de {intentos} intentos")

#Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 
#Inicializamos la variable 'numero' para tomar el 100 como punto de partida
numero = 100

#Efectuamos el bucle 'while' con la iteración solicitada
while numero >= 0:
    print(numero)
    numero=numero-2

#Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario. 
#Solicitamos el número al usuario
numero = int(input("Ingrese el número para efectuar la suma: "))

#Inicializamos la variable 'suma'
suma = 0

#Ejecutamos un bucle 'for' para efectuar la sumatoria
for iter in range(1, numero + 1):
    suma += iter

#Efectuamos la salida por pantalla mostrando el resultado de la suma
print(f"La suma de los números comprendidos entre 0 y {numero} es: {suma}")

#Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
#Inicializamos las cuatro variables que se solicitan para los resultados
pares = 0
impares = 0
positivos = 0
negativos = 0

#Efectuamos la solicitud al usuario para ingresar los 100 números de su elección
print(f"Ingrese cien números enteros:")

#Efectuamos un bucle 'for' en rango 100 para que vaya procesando los números ingresados
for iter in range(100):
    numero = int(input(f"Número {iter+1}: "))

#Mediante una condicional 'if' efectuamos la diferenciación entre pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
#Con otra condicional 'if' diferenciamos positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:     #Evitamos que se considere al 0 como positivo o negativo
        negativos += 1

#Realizamos la salida por pantalla de los resultados obtenidos tras el ingreso de los números
print("Resultados de los números ingresados:")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

#Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores
#Efectuamos la solicitud al usuario para ingresar los 100 números de su elección
print(f"Ingrese cien números enteros:")

#Inicializamos la variable 'suma' para sumar los 100 números cuya media obtendremos posteriormente
suma = 0

#Efectuamos un bucle 'for' en rango 100 para que vaya procesando los números ingresados
for iter in range(100):
    numero = int(input(f"Número {iter+1}: "))
    suma += numero

#Cargamos la división para obtener la media de los 100 números ingresados
media = suma / 100

#Mostramos la salida por pantalla de los resultados obtenidos
print("Resultados:")
print("La suma total de los números ingresados es:", suma)
print("La media entre los números ingresados es:", media)

#Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
#Solicitamos al usuario que ingrese un número de su elección
numero = int(input("Ingrese un número entero: "))

#Tomamos el valor absoluto del número ingresado, en caso de que sea negativo
abs = abs(numero)  # trabajamos con el valor absoluto para manejar negativos

#Inicializamos la variable para el número invertido
invertido = 0

#Ejecutamos un bucle 'while' para realizar las operaciones correspondientes
while abs > 0:
    digito = abs % 10           #Eliminamos el último dígito mediante el resto de la división del número por 10
    invertido = invertido * 10 + digito #Rearmamamos el número multiplicando por 10 y sumando el dígito
    abs //= 10                  #Eliminamos el último dígito del nuevo número obtenido mediante la división entera por 10

#Si el número elegido era negativo, recuperamos el signo para el resultado final
if numero < 0:
    invertido = -invertido

#Mostramos por pantalla el resultado final
print("El número invertido es:", invertido)