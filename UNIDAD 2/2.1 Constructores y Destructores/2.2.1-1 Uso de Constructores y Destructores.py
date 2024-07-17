# SEMANA 7
"""Consideremos una clase Restaurante para atender a un cliente dentro de un restaurante"""
# Creamos la clase restaurante
class Restaurante:
    # Definimos el método __init__ (constructor)
    def __init__(self,nombre, mesa, comida,bebida,postre, precio):
        self.nombre = nombre #Atributo
        self.mesa = mesa
        self.comida = comida
        self.bebida = bebida
        self.postre = postre
        self.precio = precio
    def pagar(self): # Métoco pagar
        print("El cliente canceló", self.precio, "dólares") # Imprime el precio

    #Método Destructor
    def __del__(self):
        self.precio = 12 # Cambio del precio
        print("El objeto se ha eliminado de la memoria")    
# Instancia del objeto persona 1 de la clase restaurante
cliente_1 = Restaurante("María","3", "Sopa de pollo", "jugo de maracuyá", "galletas y leche", 15)
cliente_1.pagar() # LLama al método pagar
# Eliminación de objetos (para mostrar el uso de destructores)
del cliente_1