#Ejercicio1: Crear archivo inicial productos.txt
with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,350.0,15\n")
    archivo.write("Regla,90.0,40\n")
print("Archivo 'productos.txt' creado correctamente.")

#Ejercicio2: Crear programa para leer y mostrar productos
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#Ejercicio3: Agregar productos desde teclado, sin que se borre el archivo existente
nombre = input("Ingrese nombre del producto: ")
precio = input("Ingrese precio: ")
cantidad = input("Ingrese cantidad: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print("Producto agregado correctamente.")        

#Ejercicio4: Cargar productos en una lista de diccionarios
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()       
        datos = linea.split(",")    
        
        producto = {
            "nombre": datos[0],
            "precio": datos[1],   
            "cantidad": datos[2]   
        }
        
        productos.append(producto)

for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

#Ejercicio5: Buscar producto por nombre
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False

for p in productos:
    if p["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")

#Ejercicio6: Guardar productos actualizados
with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']} | ${p['precio']} | {p['cantidad']}\n")

print("Archivo 'productos.txt' actualizado correctamente.")