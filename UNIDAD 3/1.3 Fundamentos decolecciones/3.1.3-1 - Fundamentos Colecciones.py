# SEMANA 11
'''Desarrollar un sistema avanzado de gestión de inventarios para una tienda, que incorpore las colecciones en POO para un manejo eficiente de los ítems del inventario y almacene la información del inventario en archivos.'''
# Clase Producto
import os
class Producto:
  def __init__(self, id, nombre, cantidad, precio): # Constructor
    self.id = id # Atributo id
    self.nombre = nombre # Atributo nombre
    self.cantidad = cantidad # Atributo cantidad
    self.precio = precio # Atributo precio

  def __str__(self): # Método para mostrar los datos del producto
    return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

# Clase Inventario
class Inventario:
  def __init__(self):
    self.productos = {} # Diccionario para almacenar los productos
    self.cargar_inventario() # Llama al método para cargar el inventario desde el archivo

  def cargar_inventario(self): # Método para cargar el inventario desde el archivo
    try: # Intenta abrir el archivo
      if not os.path.exists("Inventario_11.txt"): # Si el archivo no existe
        with open("Inventario_11.txt", "w") as archivo: # Crea el archivo
          archivo.write("ID,Nombre,Cantidad,Precio\n") # Escribe la cabecera del archivo
      else:
        with open("Inventario_11.txt", "r") as archivo: # Si el archivo existe
          for linea in archivo: # Recorre cada línea del archivo
            id, nombre, cantidad, precio = linea.strip().split(",") # Separa los datos por coma
            self.productos[id] = Producto(id, nombre, int(cantidad), float(precio)) # Crea un objeto Producto y lo agrega al diccionario


    except FileNotFoundError: # Si el archivo no existe
      print("El Inventario no existe.") # Imprime un mensaje de error

  def guardar_inventario(self): # Método para guardar el inventario en el archivo
    with open("Inventario_11.txt", "w") as archivo: # Abre el archivo en modo escritura
      for producto in self.productos.values(): # Recorre cada producto en el diccionario
        archivo.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n")
  
  def agregar_producto(self, producto): # Método para agregar un producto al inventario
    if producto.id in self.productos:
      print(f"El producto con ID {producto.id} ya existe en el inventario.")

    else: # Si el producto no existe en el inventario
      self.productos[producto.id] = producto # Agrega el producto al diccionario
      self.guardar_inventario() # Guardar los cambios en el archivo
      print("Se agregó un producto al inventario") 

  def eliminar_producto(self, id): # Método para eliminar un producto del inventario
    if id in self.productos: # Si el producto existe en el inventario
      del self.productos[id] # Elimina el producto del diccionario
      self.guardar_inventario() # Guardar los cambios en el archivo
      print("Se eliminó un producto del inventario")
    else:
      print(f"No se encontró un producto con ID {id} en el inventario.")

  def actualizar_precio(self, id, precio): # Método para actualizar el precio de un producto
    if id in self.productos: # Si el producto existe en el inventario
      self.productos[id].precio = precio # Actualiza el precio del producto
      self.guardar_inventario() # Guardar los cambios en el archivo
      print("Se actualizó el precio del producto.")

    else: 
      print(f"No se encontró un producto con ID {id} en el inventario.")

  def buscar_producto_nombre(self, nombre): # Método para buscar un producto por nombre
    resultados = [] # Lista para almacenar los resultados de la búsqueda
    for producto in self.productos.values(): # Recorre cada producto en el diccionario
      if producto.nombre.lower() == nombre.lower(): # Si el nombre del producto coincide con el nombre buscado
        resultados.append(producto) # Agrega el producto a la lista de resultados

    return resultados # Devuelve la lista de resultados

  def mostrar_inventario(self): # Método para mostrar el inventario
    for productos in self.productos.values(): # Recorre cada producto en el diccionario
      print(productos)

    

# Creación del Menú
def menu(): # Función para mostrar el menú
  print("1. Agregar producto")
  print("2. Eliminar producto")  
  print("3. Actualizar producto")
  print("4. Buscar producto")
  print("5. Mostrar inventario")
  print("6. Salir")

inventario = Inventario() # Creación del inventario
while True:
  menu() # Mostrar el menú
  opcion = input("Ingrese una opción: ")

  if opcion == "1": # Opción 1: Agregar producto
    id = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    producto = Producto(id, nombre, cantidad, precio)
    inventario.agregar_producto(producto)

  elif opcion == "2": # Opción 2: Eliminar producto
    id = input("Ingrese el ID del producto a eliminar: ")
    inventario.eliminar_producto(id)

  elif opcion == "3": # Opción 3: Actualizar producto
    id = input("Ingrese el ID del producto: ")
    precio = float(input("Ingrese el nuevo precio del producto: "))
    inventario.actualizar_precio(id, precio)
    inventario.guardar_inventario()
  
  elif opcion == "4": # Opción 4: Buscar producto
    
    nombre = input("Ingrese el nombre del producto a buscar: ")
    resultados = inventario.buscar_producto_nombre(nombre)
    if resultados: 
      print("Productos encontrados:")
      for producto in resultados: 
        print(producto)

    else:
      print("No se encontraron productos con ese nombre.")

  elif opcion == "5": # Opción 5: Mostrar inventario
    inventario.mostrar_inventario()

  elif opcion == "6": # Opción 6: Salir
    break

  else: # Opción inválida
    print("Opción inválida")