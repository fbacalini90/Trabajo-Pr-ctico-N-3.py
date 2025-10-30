#Ejercicio1: Cálculo del factorial de un número
#Importamos el módulo sys y le establecemos un límite
import sys
sys.setrecursionlimit(20000)
#Generamos la función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:  #Determinamos el caso base
        return 1
    else:
        return n * factorial(n - 1)  #Efectuamos la llamada recursiva
#Solicitamos al usuario que ingrese un número
num = int(input("Ingrese un número para conocer los factoriales entre 1 y su valor (máximo 20000): "))
#Mediante un for efectuamos la operación y mostramos el resultado por pantalla
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}")

#Ejercicio2: Cálculo del valor de la serie Fibonacci hasta posición especificada por el usuario
#DEfinimos la función para calcular la serie Fibonacci hasta un valor establecido
def fibonacci_recursivo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

#Solicitamos al usuario hasta qué posición quiere ver la serie
n = int(input("Ingrese hasta qué posición desea mostrar la serie de Fibonacci: "))

#Mostramos la serie completa
print("Serie de Fibonacci hasta la posición", n, ":")
for i in range(n + 1):
    print(fibonacci_recursivo(i))

#Ejercicio3: Cálculo de la potencia de un número según la fórmula n^m=n*n^(n-1)
#Definimos la función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0: #Caso base
        return 1
    else:              #Caso recursivo
        return base * potencia(base, exponente - 1)

#Definimos el algoritmo general, solicitando los valores deseados por el usuario
def algoritmo_general():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))

    resultado = potencia(base, exponente)

#Salida con el resultado por pantalla
    print(f"{base} elevado a la {exponente} es: {resultado}") 

#Llamamos al algoritmo general
algoritmo_general()

#Ejercicio4: Conversión de un número decimal a binario, expresado como cadena
#Definimos la función recursiva que convierte entero a binario
def binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return binario(num // 2) + str(num % 2)

#Solicitud al usuario para que ingrese el número que desea convertir
num = int(input("Ingrese el número que desea convertir a binario: "))

#Llamada a la función
binario_cadena = binario(num)

#Salida con el resultado por pantalla
print(f"El binario de {num} es: {binario_cadena}")

#Ejercicio5: Función recursiva para determinar si una palabra o cadena es palíndromo
#Definimos la función para adaptar la palabra 
def palabra_adaptada(palabra):
    palabra = "".join(palabra.split())  #Quitamos los espacios
    #Quitamos tildes para el caso que se utilice un palíndromo que los tenga
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")
    return palabra

#Definimos la funcion para verificar si hay o no palíndromo
def es_palindromo(palabra):
    palabra = palabra_adaptada(palabra)
    if len(palabra) <= 1:
        return True 
    if palabra[0] != palabra[len(palabra) - 1]:
        return False
    else:
       return es_palindromo(palabra[1:len(palabra) - 1])

#Solicitamos al usuario que ingrese una palabra para determinar si es palíndromo
palabra = input("Ingrese una palabra para determinar si es o no un palíndromo: ").lower()

#Llamada a la funcion
respuesta = es_palindromo(palabra)

#Salida con el resultado por pantalla
if respuesta == False:
    print(f"'{palabra}' no es palíndromo")
else:
    print(f"'{palabra}' es palindromo")

#Ejercicio6: Función recursiva para calcular la suma de dígitos de un número entero
#Definimos la función para sumar los dígitos
def suma_digitos(n):
    #Caso base (si el número elegido tiene un solo dígito)
    if n < 10:
        return n
    else:
        #Caso recursivo (suma del último dígito con la suma del resto)
        return (n % 10) + suma_digitos(n // 10)

#Solicitud al usuario para que ingrese el número
n = int(input("Ingrese el número que desea sumar sus cantidad de digitos: "))

#Llamada a la función
suma = suma_digitos(n)

#Salida con el resultado por pantalla
print(f"La suma de los dígitos de {n} es {suma}.")

#Ejercicio7: Función que resuelva cuántos bloques son necesarios para construir una pirámide dando la cantidad de la base
#Definimos la funcion
def contar_bloques(n):
    if n == 1:           #Caso base
        return 1
    else:                #Caso recursivo
        return n + contar_bloques(n - 1)
    
#Solicitud al usuario de cuántos bloques utilizará en la base
n = int(input("¿Cuántos bloques utilizarás en la base de tu pirámide? "))

#Llamada a la funcion
bloques = contar_bloques(n)

#Salida con el resultado por pantalla
print(f"La cantidad de bloques necesarios es: {bloques}")

#Ejercicio8: Función para contar cuántas veces aparece un dígito en un número
#Definimos la función
def contar_digito(numero, digito):
    if numero == 0:                                        #Caso base
        return 0
    ultimo_digito = numero % 10                            #Obtenemos el ultimo número mediante el resto de su división por 10
    if ultimo_digito == digito:                            
        return 1 + contar_digito(numero // 10, digito)     #Caso recursivo
    else:
        return contar_digito(numero // 10, digito)
    
#Solicitud al usuario para que ingrese un número
numero = int(input("Ingrese un número: "))

#Verificación de que haya ingresado un dígito y no un número de más de una cifra
while True:
    digito = int(input(f"Ingrese un dígito (del 0 al 9) para contar cuántas veces aparece en {numero}: "))
    if digito >= 0 and 9 >= digito:
        break
    else:
        print("Número no válido (debe ingresar sólo un dígito).")
        continue 

#Llamada a la función
resultado = contar_digito(numero, digito)

#Salida por pantalla con el resultado
print(f"El {digito} aparece {resultado} veces en el número {numero}")