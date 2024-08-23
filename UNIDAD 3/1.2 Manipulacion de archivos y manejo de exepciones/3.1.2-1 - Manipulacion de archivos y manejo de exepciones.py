# SEMANA 10 
'''Manipulación de archivos y manejo de excepciones'''

# Clase Producto
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
    self.productos = [] #Lista de productos
    self.cargar_inventario() # Cargar inventario desde un archivo

  def cargar_inventario(self): # Método para cargar el inventario desde un archivo
    with open("Inventario.txt", "r") as archivo: # Abrir el archivo en modo lectura
      for linea in archivo:
        id, nombre, cantidad, precio = linea.strip().split(",") # Separar los datos por comas
        self.productos.append(Producto(id, nombre, int(cantidad), float(precio))) # Agregar el producto a la lista


  def guardar_inventario(self): # Método para guardar el inventario en un archivo
    with open("Inventario.txt", "w") as archivo: # Abrir el archivo en modo escritura
      for producto in self.productos:
        archivo.write(f"{producto.id},{producto.nombre},{producto.cantidad},{producto.precio}\n") # Escribir los datos del producto en el archivo

  def agregar_producto(self, producto): # Método para agregar productos
    self.productos.append(producto) # Agregar producto a la lista
    self.guardar_inventario() # Guardar los cambios en el archivo
    print("Se agregó un producto al inventario") 

  def eliminar_producto(self, id): # Método para eliminar productos
    for producto in self.productos:
      if producto.id == id:
        self.productos.remove(producto) # Eliminar producto de la lista
        self.guardar_inventario() # Guardar los cambios en el archivo
        print("Se eliminó un producto del inventario")
        break

  def actualizar_producto(self, id, nombre, cantidad, precio): # Método para actualizar productos
    for producto in self.productos: # Recorrer la lista de productos
      if producto.id == id: 
        producto.nombre = nombre # Actualizar nombre del producto
        producto.cantidad = cantidad # Actualizar cantidad del producto
        producto.precio = precio # Actualizar precio del producto
        print("Producto actualizado exitosamente")
        break

  def buscar_producto(self): # Método para buscar productos
    id = input("Ingrese el ID del producto: ") # Pedir al usuario el ID del producto
    for producto in self.productos: # Recorrer la lista de productos
      if producto.id == id: # Buscar el producto por ID 
        print(producto)
        break

  def mostrar_inventario(self): # Método para mostrar el inventario
    for productos in self.productos: # Recorrer la lista de productos
      print(productos.id, productos.nombre, productos.cantidad, productos.precio) # Mostrar los datos del productos

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
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    precio = input("Ingrese el precio del producto: ")
    inventario.actualizar_producto(id, nombre, cantidad, precio)


  elif opcion == "4": # Opción 4: Buscar producto
    nombre = input("Ingrese el nombre del producto a buscar: ")
    inventario.buscar_producto()

  elif opcion == "5": # Opción 5: Mostrar inventario
    inventario.mostrar_inventario()

  elif opcion == "6": # Opción 6: Salir
    break

  else: # Opción inválida
    print("Opción inválida")