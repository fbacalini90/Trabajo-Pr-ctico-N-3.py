#Ejercicio 1: "Hola Mundo!"
#Definimos la función
def imprimir_hola_mundo():
    return "Hola Mundo!"

#Programa global
print(imprimir_hola_mundo())

#Ejercicio 2: Saludar al usuario
#Definimos la función
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"

#Programa global
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo) 

#Ejercicio 3: Información personal
#Definimos la función
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

#Programa global
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

salida = informacion_personal(nombre, apellido, edad, residencia)
print(salida)

#Ejercicio 4: Área y perímetro del círculo
import math #Importamos la galería 'math' para tener precisión en el valor de pi

#Definimos las funciones y cargamos las fórmulas matemáticas
def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def area_perimetro(radio):
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El radio de su círculo es: {radio} cm.")
    print(f"El área de su círculo es de {area} cm2.")
    print(f"El perímetro de su círculo es de {perimetro} cm.")

#Programa global
print("OBTENGA EL ÁREA Y PERÍMETRO DE UN CÍRCULO")
radio = float(input("Ingrese el radio del círculo en centímetros: "))
area_perimetro(radio)

#Ejercicio 5: Segundos a horas
#Definimos la función
def segundos_a_horas(segundos):
    return segundos / 3600

#Programa global
print("CONVERSOR DE SEGUNDOS A HORAS")
segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas} horas.")

#Ejercicio 6: Tabla de multiplicación
#Definimos la función
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#Programa global
print("GENERADOR DE TABLAS DE MULTIPLICACIÓN")
numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)

#Ejercicio 7: Operaciones básicas
#Definimos la función
def operaciones_basicas (a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b if b != 0 else "Error. No se puede dividir por cero."
    return (suma, resta, producto, division)

#Programa global
print("OPERACIONES BÁSICAS ENTRE DOS NÚMEROS")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

resultado = operaciones_basicas(a, b)

#Mostramos los resultados utilizando una tupla
print(f"El resultado de la suma es: {resultado[0]}")
print(f"El resultado de la resta es: {resultado[1]}")
print(f"El resultado de la multiplicación es: {resultado[2]}")
print(f"El resultado de la división es: {resultado[3]}")

#Ejercicio 8: Calculadora de Índice de Masa Corporal
#Definimos la función
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

#Programa global
print("CALCULE SU ÍNDICE DE MASA CORPORAL (IMC)")
peso = float(input("Ingrese su peso en kilogramos (ej.: 86.5): "))
altura = float(input("Ingrese su altura en metros (ej.: 1.90): "))

imc = calcular_imc(peso, altura)

print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

#Ejercicio 9: Pasaje de Celsius a Fahrenheit
#Definimos la función
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Programa global
print("CONVERSOR DE GRADOS CELSIUS (°C) A FAHRENHEIT (°F)")
celsius = float(input("Ingrese la temperatura en grados Celsius (°C): "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#Ejercicio 10: Promedio entre tres números
#Definimos la función
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa global
print("CALCULADOR DE PROMEDIO ENTRE TRES NÚMEROS")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de los tres números elegidos es {promedio:.2f}")