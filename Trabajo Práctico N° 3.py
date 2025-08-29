#Ejercicio 1 Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 
#Inicializamos la variable edad mínima, para establecer la mayoría de edad
edad_minima = 18
#Efectuamos la solicitud al usuario para que indique su edad
edad = int(input("Ingrese su edad: "))
#Ejecutamos la condicional
if edad >= edad_minima:
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad")   

#Ejercicio 2 Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 
#Inicializamos la variable "aprobación" para establecer la nota de aprobado
aprobacion = 6
#Efectuamos la solicitud al usuario para que indique su nota
nota = int(input("Ingrese su nota: "))
#Ejecutamos la condicional
if nota >= aprobacion:
    print("Aprobado")
else:
    print("Desaprobado") 

#Ejercicio 3  Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par"
#Solicitud al usuario para que ingrese un número, adaptando lo trabajado con el bucle "Mientras" en PSeInt
while True:
    numero = int(input("Ingrese un número: "))
#Ejecución de la condicional    
    if numero % 2 == 0:
        print("Ha ingresado un número par")
        break  #Para terminar el bucle si el número elegido es par
    else:
        print("Por favor, ingrese un número par") #Para solicitar otro número en caso de haber elegido uno que no es par  

#Ejercicio 4 Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál categoría pertenece
#Solicitud al usuario para que indique su edad
edad = int(input("Ingrese su edad: "))
#Ejecución de la condicional para determinar el rango de edad
if edad > 0 and edad < 12:
    print("Usted es un niño")
elif edad >= 12 and edad < 18:
    print("Usted es un adolescente")
elif edad >= 18 and edad < 30:
    print("Usted es un adulto joven")
elif edad >= 30:
    print("Usted es un adulto")
else:
    print("La edad ingresada es incorrecta") #Con el objetivo de evitar que se tome una edad erróneamente de ingresarse un número negativo, tal lo visto en la Pregunta 4 de la Actividad III   

#Ejercicio 5 Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
#Solicitud al usuario para que ingrese una contraseña, adaptando lo trabajado con el bucle "Mientras" en PSeInt
while True:
    contraseña = input("Ingrese una contraseña: ")
#Ejecución de la condicional para validar o no la contraseña elegida
    if 8 <= len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta")
        break   #Concluye la ejecución al ingresarse una contraseña válida
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres") #Solicitud de repetir la contraseña al no entrar dentro del rango de caracteres requerido

#Ejercicio 6 escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
#Efectuamos la importación del paquete "statistics" y definimos la variable
import statistics as stats
#Definimos la lista de números aleatorios según se solicita en la consigna
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Realizamos los cálculos estadísticos tal y como se explican en la web de Python
media = stats.mean(numeros_aleatorios)
mediana = stats.median(numeros_aleatorios)
moda = stats.mode(numeros_aleatorios)
#Solicitamos al programa que muestre por pantalla los resultados de los cálculos efectuados en el paso anterior
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
#Ejecución de la condicional para determinar el sesgo
if media > mediana > moda:
    print("La distribución tiene sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("La distribución no tiene sesgo")

#Ejercicio 7 Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final 
# Definición de las vocales como variable
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
#Solicitud al usuario para que ingrese la palabra o frase de su elección
palabra_o_frase = input("Ingrese una palabra o frase: ")
#Ejecución de la condicional verificando si la palabra o frase elegida termina en vocal
if palabra_o_frase[-1] in vocales:
    print (palabra_o_frase+"!")
else:
    print(palabra_o_frase)

#Ejercicio 8 Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee
#Solicitud de los datos requeridos al usuario
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese el número de opción (1: todo en mayúsculas, 2: todo en minúsculas, 3: primera letra en mayúscula): ")
#Ejecución de la condicional
if opcion == "1":
    print("Resultado:", nombre.upper())   #Para escribir todo el nombre en mayúsculas
elif opcion == "2":
    print("Resultado:", nombre.lower())   #Para escribir todo el nombre en minúsculas
elif opcion == "3":
    print("Resultado:", nombre.title())   #Para escribir todo el nombre con la primera letra en mayúsculas
else:
    print("Opción inválida. Debe ingresar 1, 2 o 3.") #Por si el usuario ingresa una opción errónea

#Ejercicio 9  Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla.
#Solicitud al usuario para que el grado de terremoto según la escala de Richter
categoria = int(input("Ingrese el grado del terremoto según la escala de Richter: "))
#Ejecución de la condicional para determinar el rango de gravedad del terremoto
if categoria > 0 and categoria < 3:
    print("Muy leve. El terremoto es imperceptible.")
elif categoria >= 3 and categoria < 4:
    print("Leve. El terremoto es ligeramente perceptible")
elif categoria >= 4 and categoria < 5:
    print("Moderado. El terremoto es perceptible, pero no causará daños.")
elif categoria >= 5 and categoria < 6:
    print("Fuerte. El terremoto puede causar daños en estructuras débiles.")
elif categoria >= 6 and categoria < 7:
    print("Muy Fuerte. El terremoto puede causar daños significativos.")
elif categoria >= 7:
    print("Extremo. El terremoto puede causar daños graves a gran escala.")           
else:
    print("La categoría ingresada es incorrecta") #Con el objetivo de evitar que se tome una categoría erróneamente de ingresarse un número negativo   

#Ejercicio 10 Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano. 
# Solicitar datos al usuario acerca de en qué hemisferio se encuentra y qué día es
dia = int(input("Ingrese el día del mes: "))
mes = int(input("Ingrese el mes del año: "))
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").strip().upper()
#Se inicializa la variable "estación" para que sea determinada y mostrada en pantalla
estacion = ""
#Ejecución de la condicional
if hemisferio == "N": #Carga de datos correspondientes a las fechas para el hemisferio norte
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia < 21):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia < 21):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 21):
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif hemisferio == "S": #Carga de datos correspondientes a las fechas para el hemisferio sur
    if (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia < 21):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia < 21):
        estacion = "Primavera"
    elif (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia < 21):
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:
    print("Hemisferio inválido. Debe ser 'N' o 'S'.")
#Mostrar el resultado
if estacion:
    print(f"Usted se encuentra en {estacion}.")         