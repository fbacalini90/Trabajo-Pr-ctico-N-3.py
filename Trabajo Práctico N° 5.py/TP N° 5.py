#Ejercicio 1: Crear una lista con las notas de  10 estudiantes mostrándola completa, calculando y mostrando el promedio e indicando nota más alta y más baja.
#Creamos una lista vacía para que luego se le vayan cargando las notas
notas = []

#Generamos un bucle 'for' para ir cargando las notas
for iter in range(10):
    nota = float(input(f"Ingrese la nota del estudiante {iter+1}: "))
    notas.append(nota)

#Mostramos por pantalla la lista completa
print("Notas de los diez estudiantes seleccionados: ", notas)

#Efectuamos el cálculo del promedio, mostrando la salida por pantalla
promedio = sum(notas) / len(notas)
print("El promedio de las notas ingresadas es: ", promedio)

#Mostramos la nota más alta y más baja registradas
print("Nota más alta: ", max(notas))
print("Nota más baja: ", min(notas))


#Ejercicio 2: Pedir al usuario que cargue 5 productos, mostrando la lista ordenada alfabéticamente mediante la función 'sorted' y permitir eliminación de algún producto de la lista
#Creamos una lista vacía para que luego se le vayan cargando los productos
productos = []

#Solicitamos la carga de los productos mediante un bucle 'for'
for iter in range (5):
    prod = input(f"Ingrese el producto {iter+1}: ")
    productos.append(prod)

#Mostramos la lista agregando la función 'sorted' para ordenarla alfabéticamente, lo cual mantendremos en todos los casos posteriores
print("Los productos ingresados a la lista son: ", sorted(productos))

#Preguntamos si se desea eliminar algún producto
eliminar = input("¿Desea eliminar algún producto de la lista? Ingrese el nombre del que desee eliminar, de lo contrario presione enter: ")
#Mediante un 'if' hacemos la diferenciación en caso de desearse eliminar o no algún producto
if eliminar == "":
    print("No se eliminó ningún producto, los existentes en la lista son: ", sorted(productos))
else:
    if eliminar in productos:
        productos.remove(eliminar)
        print("El producto ha sido eliminado")
        print("Los productos restantes en la lista son: ", sorted(productos))
    else:
        print("El producto ingresado no forma parte de la lista")       


#Ejercicio 3: Generar una lista con 15 números al azar entre 1 y 100, creando una lista de pares e impares y mostrando cuántos números tiene cada una
#Importamos la biblioteca 'random' para poder generar lista de números aleatorios
import random

#Generamos la lista de 15 números con las características solicitadas
numeros = [random.randint(1, 100) for num in range (15)]
print("Los números son: ", numeros)

#Creamos la lista de pares e impares
pares = []
impares = []

#Generamos un 'if' para hacer la diferenciación entre pares e impares
for num in numeros:
    if num % 2 == 0:
           pares.append(num)
    else:
           impares.append(num) 

#Realizamos la salida por pantalla con los números agrupados
print("Los números pares son :", pares)
print(f"Hay {len(pares)} números pares")

print("Los números impares son: ", impares)
print(f"Hay {len(impares)} números impares")


#Ejercicio 4: Dada una lista con valores repetidos, crearla sin los elementos repetidos y mostrar el resultados
#Creamos una lista con valores que se repiten
valores = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

#Mostramos la lista original por pantalla
print("Lista original: ", valores)

#Generamos un 'for' para crear la lista sin repetidos
sin_repetidos = []
for val in valores:
    if val not in sin_repetidos:
        sin_repetidos.append(val)

#Mostramos la salida por pantalla
print("Lista sin repetidos: ", sin_repetidos)


#Ejercicio 5: Crear una lista con los nombres de 8 estudiantes presentes en una clase, preguntando al usuario si quiere agregar o eliminar a alguno y mostrando la actualización
#Creamos la lista con los 8 estudiantes y mostramos por pantalla
estudiantes = ["Ana", "Juan", "María", "Pedro", "Jimena", "Matías", "Romina", "Cristian"]
print("Lista de estudiantes: ", estudiantes)

#Preguntar al usuario si desea agregar o eliminar a alguno
opcion = input("¿Desea agregar o eliminar a algún estudiante de la lista (escriba agregar o eliminar, o presione enter en caso de que no)").lower()

#Generamos un 'if' para proceder según la opción elegida
if opcion == "":
    print("No se agregó o eliminó a ningún estudiante")
    print("La Lista de estudiantes es: ", estudiantes)

elif opcion == "agregar":
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
    print(f"Se agregó a {nuevo_estudiante}")
    print("La Lista de estudiantes es: ", estudiantes)

elif opcion == "eliminar":
    eliminado = input("Ingrese el nombre del estudiante a eliminar: ")
    estudiantes.remove(eliminado)    
    print(f"Se eliminó a {eliminado}")
    print("La Lista de estudiantes es: ", estudiantes)
else:
    print("Error. Ese estudiante no está en la lista.")
    print("La Lista de estudiantes es: ", estudiantes)


#Ejercicio 6: Dada una lista con 7 números, rotar todos los elementos a una posición a la derecha (el último pasa a ser el primero)
#Generamos la lista con números
numeros = [1, 2, 3, 4, 5, 6, 7]
print("Números originales", numeros)

#Mediante un slicing los rotamos una posición a la derecha
numeros = numeros[-1:] + numeros [:-1]

#Mostramos la salida por pantalla
print(numeros)


#Ejercicio 7: Crear una matriz de 7x2 con las temperaturas mínimas y máximas de una semana, calculando el promedio de mínimas y máximas y mostrando el día de mayor amplitud térmica
#Creamos la matriz
temperaturas = [
    [12, 25], #Día1
    [15, 28], #Día2
    [11, 22], #Día3
    [14, 30], #Día4
    [13, 27], #Día5
    [16, 29], #Día6
    [10, 24], #Día7
] 

#Calculamos el promedio de mínimas
minimas = [dia[0] for dia in temperaturas]
promedio_minimas = sum(minimas) / len(minimas)

#Hacemos lo mismo con las máximas
maximas = [dia[1] for dia in temperaturas]
promedio_maximas = sum(maximas) / len(maximas)

#Calculamos la amplitud térmica de cada día
amplitudes = [dia[1] - dia [0] for dia in temperaturas]
mayor_amplitud = max(amplitudes)
dia_mayor = amplitudes.index(mayor_amplitud) + 1 #Corrigiendo para que no tome un "Día 0"

#Mostramos los resultados por pantalla
print(f"El promedio de mínimas fue: {promedio_minimas}°C")
print(f"El promedio de máximas fue: {promedio_maximas}°C")
print(f"La mayor amplitud térmica fue de {mayor_amplitud}°C el día {dia_mayor}")


#Ejercicio 8: Crear una matriz con las notas de 5 estudiantes en 3 materias mostrando el promedio de cada estudiante y cada materia
#Creamos listas con los nombres de los estudiantes y las materias
estudiantes = ["María", "Juan", "Ana", "Pedro", "Patricia"]
materias = ["Matemática", "Historia", "Biología"]

#Creamos la matriz con las notas en cada materia de cada estudiante
notas = [
    [7, 8, 6], #María
    [5, 9, 8], #Juan
    [6, 7, 7], #Ana
    [9, 5, 7], #Pedro
    [6, 8, 6], #Patricia
]

#Generamos un 'for' para calcular el promedio de cada estudiante y lo mostramos en pantalla
print("Promedio de los estudiantes:")
for alumno, fila in enumerate(notas):
    prom_e = sum(fila) / len(fila)
    print(f"{estudiantes[alumno]:}: {prom_e}")
    

#Hacemos lo mismo para cada materia
print("Promedio por cada materia:")
for materia in range(len(materias)):
    columna = [notas[alumno][materia] for alumno in range(len(estudiantes))]
    prom_m = sum(columna) / len(columna)
    print(f"{materias[materia]}: {prom_m}")


#Ejercicio 9: Representar un tablero de ta-te-ti como una lista de listas, con guiones representando las casillas vacías, permitiendo que dos jugadores ingresen posiciones y mostrando el tablero después de cada jugada
#Solicitamos a los jugadores que ingresen su nombre y los asignamos al símbolo que van a utilizar
nombre_x = input("Nombre del jugador que usará 'X': ")
nombre_o = input("Nombre del jugador que usará 'O': ")
nombres = {"X": nombre_x, "O": nombre_o}

#Creamos el tablero vacío con guiones marcando cada posición de juego
tablero = [["-" for _ in range(3)] for _ in range(3)]

#Establecemos los turnos y mostramos el tablero vacío para iniciar el juego con un 'for'
turnos = ["X", "O"]
for fila in tablero:
    print(" ".join(fila))
print()

#Generamos el bucle con la iteración para alternar los turnos hasta el rango máximo posible de jugadas
for i in range(9):
    simbolo = turnos[i % 2]         
    nombre_actual = nombres[simbolo]

#Generamos mediante un 'while' la solicitud para indicar posición de fila y columna para cada jugada, evitando que el usuario indique un rango fuera del tablero o superponga una jugada anterior
    while True:
        fila = int(input(nombre_actual + " (" + simbolo + "), ingresá fila (0-2): "))
        col = int(input(nombre_actual + " (" + simbolo + "), ingresá columna (0-2): "))
        if fila not in [0,1,2] or col not in [0,1,2]:
            print("Indicaste una posición fuera del tablero. Intentalo de nuevo.")
        elif tablero[fila][col] != "-":
            print("Esa casilla ya está ocupada. Intentalo de nuevo.")
        else:
            tablero[fila][col] = simbolo
            break

#Mostramos el tablero actualizado luego de cada jugada
    for f in tablero:
        print(" ".join(f))
    print()

#Verificamos si hay ganador mediante la coincidencia de su símbolo tres veces
    ganador = False
    #Horizontal
    for f in tablero:
        if f[0] == f[1] == f[2] == simbolo:
            ganador = True
    #Vertical
    for c in range(3):
        if tablero[0][c] == tablero[1][c] == tablero[2][c] == simbolo:
            ganador = True
    #Diagonal
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == simbolo:
        ganador = True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == simbolo:
        ganador = True

#Mostramos mensaje anunciando al ganador
    if ganador:
        print("Felicitaciones, " + nombre_actual + ". ¡Ganaste la partida!")
        break

#Mostramos mensaje en caso de terminarse el juego sin un ganador
    if i == 8:
        print("Fin del juego. ¡Tenemos un empate!")


#Ejercicio 10: Registro de ventas de 4 productos durante 7 días, mostrando el total vendido por producto, el día con mayores ventas y el producto más vendido de la semana
#Generamos lista con cada día de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

#Solicitamos nombre de cada producto a registrar mediante un 'for'
productos = []
for i in range(4):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(nombre)

#Le damos forma a la matriz, solicitando además al usuario el ingreso de ventas de cada producto en un día en particular
ventas = []
for i in range(4):
    fila = []
    for j in range(7):
        cantidad = int(input(f"Ingrese ventas de {productos[i]} en {dias[j]}: "))
        fila.append(cantidad)
    ventas.append(fila)

#Mostramos por pantalla el total de ventas de cada producto en cada semana
print("Total vendido por producto en la semana:")
totales_productos = []
for i in range(4):
    total = sum(ventas[i])
    totales_productos.append(total)
    print(f"{productos[i]}: {total}")

#Marcamos cuál fue el día con más ventas
totales_dias = []
for j in range(7):
    total_dia = sum(ventas[i][j] for i in range(4))
    totales_dias.append(total_dia)
dia_max = max(totales_dias)
indice_dia = totales_dias.index(dia_max)
print(f"El día de mayor ventas fue: {dias[indice_dia]} ({dia_max} ventas)")

#Indicamos cuál fue el producto más vendido
max_producto = max(totales_productos)
indice_prod = totales_productos.index(max_producto)
print(f"El producto más vendido fue: {productos[indice_prod]} ({max_producto} ventas)") 