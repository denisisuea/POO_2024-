# SEMANA 4
# Clase Producto que representa un producto en la tienda Marcelita
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Stock: {self.stock} unidades"

    # Método para actualizar el stock después de una compra
    def actualizar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False


# Clase Cliente que representa a un cliente de la tienda
class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pedidos = []  # Lista para almacenar los pedidos realizados por el cliente

    def __str__(self):
        return f"Cliente: {self.nombre}, Dirección: {self.direccion}"

    # Método para agregar un pedido a la lista de pedidos del cliente
    def realizar_pedido(self, pedido):
        self.pedidos.append(pedido)
        return True


# Clase Pedido que representa un pedido realizado por un cliente
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []  # Lista para almacenar los productos del pedido

    def agregar_producto(self, producto, cantidad):
        if producto.actualizar_stock(cantidad):
            self.productos.append((producto, cantidad))
        else:
            print(f"No hay suficiente stock de {producto.nombre} para añadir {cantidad} unidades.")

    def total_pedido(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos)
        return total

    def __str__(self):
        detalle_productos = "\n".join([f"{producto.nombre} - Cantidad: {cantidad}" for producto, cantidad in self.productos])
        return f"Pedido para {self.cliente.nombre}:\n{detalle_productos}\nTotal: ${self.total_pedido()}"


# Crear algunos productos
producto1 = Producto("Laptop", 1200.00, 10)
producto2 = Producto("Smartphone", 800.00, 20)
producto3 = Producto("Tablet", 300.00, 15)

# Crear un cliente
cliente1 = Cliente("Denisis Portilla", "123 Calle Mirador")

# Crear un pedido para el cliente
pedido1 = Pedido(cliente1)

# Agregar productos al pedido
pedido1.agregar_producto(producto1, 2)
pedido1.agregar_producto(producto2, 1)

# Cliente realiza el pedido
cliente1.realizar_pedido(pedido1)

# Imprimir detalles del pedido
print(pedido1)

# Imprimir detalles del cliente
print(cliente1)