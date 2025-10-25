#Ejercicio 1: Diccionario inicial precios_frutas con artículos agregados
#Establecemos el diccionario original 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#Agregamos las otras frutas con su respectivo precio
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300 

#Salida por pantalla
print("Lista de precios:")
print(precios_frutas)

#Ejercicio 2: Actualización de precios en base al Ejercicio 1
#Establecemos el diccionario original 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#Agregamos las otras frutas con su respectivo precio
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300 

#Salida por pantalla
print("Lista de precios:")
print(precios_frutas)

#Actualización de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#Salida con los precios actualizados
print("Lista de precios actualizada:")
print(precios_frutas)

#Nota: Se establece dos veces el 'print' para que puedan observarse los cambios

#Ejercicio 3: Continuando el ejemplo anterior, creación de una lista sin los precios
#Tomamos el diccionario como había quedado del ejercicio anterior
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

# Creamos una lista solo con las frutas
frutas = list(precios_frutas.keys())

#Salida por pantalla
print("Lista de frutas:")
print(frutas)

#Ejercicio4 Programa para almacenar y consultar números telefónicos
#Creamos un diccionario vacío donde se cargarán los contactos
agenda = {}

#Solicitud al usuario para que cargue sus cinco contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    agenda[nombre] = numero

#Salida por pantalla con la confirmación
print("La agenda se ha cargado correctamente")
print(agenda)

#Opción para consultar un número
consulta = input("Ingresá el nombre del contacto que querés buscar: ")

#Salida por pantalla de la consulta efectuada
if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print("Ese contacto no está en la agenda.")

#Ejercicio5 Conteo de palabras únicas y cantidad de veces usada en una frase
#Solicitamos una frase al usuario
frase = input("Ingresá una frase: ")

#Separamos la frase en palabras y convertimos a minúsculas las palabras para no perjudicar el conteo
frase = frase.lower()
palabras = frase.split()

#Creamos un diccionario con las palabras únicas
palabras_unicas = set(palabras)

#Creamos otro diccionario con el recuento de palabras
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

#Salida por pantalla del resultado
print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento}")

#Ejercicio6 Ingresar nombres y notas de tres alumnos cargadas en una tupla, luego mostrar sus promedios
#Creamos un diccionario vacío
alumnos = {}

#Solicitud de los datos de tres alumnos y sus notas
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    print(f"Ingresá las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

#Guardamos las notas en una tupla
    alumnos[nombre] = (nota1, nota2, nota3)

#Mostramos el promedio de cada alumno
print("Promedio de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#Ejercicio7 Diccionario de estudiantes que aprobaron cada parcial

#Ejemplo de datos aleatorios 
parcial1 = {"Ana", "Luis", "Pedro", "Sofía"}
parcial2 = {"Luis", "Jimena", "Sofía", "Pedro"}

#Estudiantes que aprobaron ambos parciales mediante intersección
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

#Estudiantes que aprobaron solo uno mediante diferencia simétrica
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

#Estudiantes que aprobaron al menos uno mediante unión
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#Ejercicio8 Diccionario con productos como clave y stock como valor
#Creamos el diccionario inicial con algunos productos y su stock
stock = {
    "Tuercas": 10,
    "Tornillos": 5,
    "Clavos": 8
}

#Mostramos el stock por pantalla
print("Stock actual:")
print(stock)

#Consultamos por un producto en particular
producto = input("\nIngresá el nombre del producto que querés consultar o modificar: ")

#Normalizamos mayúsculas/minúsculas para evitar errores inesperados
producto = producto.capitalize()

#Generamos un if para agregar stock o un nuevo producto
if producto in stock:
    print(f"El stock actual de {producto} es: {stock[producto]} unidades.")
    
    #Opción para agregar unidades de un producto existente
    agregar = int(input(f"¿Cuántas unidades querés agregar a {producto}? "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]} unidades.")
else:
    print(f"{producto} no está en el stock.")
    #Opción para agregar un nuevo producto
    nuevo_stock = int(input(f"Ingresá el stock inicial para {producto}: "))
    stock[producto] = nuevo_stock
    print(f"{producto} fue agregado con {nuevo_stock} unidades.")

#Mostramos el stock actualizado por pantalla
print("\nStock actualizado:")
print(stock)

#Ejercicio9 Agenda con claves como tupla que permitan consultar actividades
#Diccionario inicial
agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "15:00"): "Clase de inglés",
    ("Miércoles", "09:30"): "Gimnasio",
    ("Jueves", "18:30"): "Turno con odontólogo"
}

#Opción para consultar un evento
dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (por ejemplo, 10:00): ")

#Creamos la tupla clave
clave = (dia, hora)

#Verificación de si existe en la agenda mediante un if
if clave in agenda:
    print(f"En {dia} a las {hora} hay: {agenda[clave]}")
else:
    print(f"No hay eventos programados para {dia} a las {hora}.")

#Ejercicio10 Construir un diccionario que se invierta
#Diccionario original
original = {
    "Argentina": "Buenos Aires",
    "Bolivia": "La Paz",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Ecuador": "Quito",
    "Paraguay": "Asunción",
    "Perú": "Lima",
    "Uruguay": "Montevideo",
    "Venezuela": "Caracas"
}

#Creamos el diccionario invertido
invertido = {capital: pais for pais, capital in original.items()}

#Mostramos los resultados por pantalla
print("Diccionario original:")
print(original)

print("\nDiccionario invertido:")
print(invertido)    