# SEMANA 8
import os # Aqui se usa principalmente para manejar rutas de archivo 

def mostrar_codigo(ruta_script): # Ruta relativa del Archivo
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu(): # Menú interactivo para elegir script y ver su contenido
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        #--------UNIDAD 1------
        # SEMANA 2
        '1': 'UNIDAD 1/1.2 Tecnicas de Programacion/Abstracion/abstracion.py',
        '2': 'UNIDAD 1/1.2 Tecnicas de Programacion/Encapsulamiento/encapsulamiento.py',
        '3': 'UNIDAD 1/1.2 Tecnicas de Programacion/Herencia/herencia.py',
        '4': 'UNIDAD 1/1.2 Tecnicas de Programacion/Polimorfismo/polimorfismo.py',
        # SEMANA 3
        '5': 'UNIDAD 1/2.1 Programacion tradicional frente a POO/2.1-1. Ejemplo Tarea Programacion Tradicional.py',
        '6': 'UNIDAD 1/2.1 Programacion tradicional frente a POO/2.1-2. Ejemplo Tarea Programacion OO.py',
        # SEMANA 4
        '7': 'UNIDAD 1/2.2Caracteristicas de la POO/2.2-1. Ejemplos Mundo Real_POO.py',
        # SEMANA 5
        #------UNIDAD 2 --------
        '8': 'UNIDAD 2/1.1 Tipos de Datos Identificadores1/2.1.1-1 Ejemplo de Datos identificadores1.py',
        # SEMANA 6
        '9': 'UNIDAD 2/1.2 Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-1 Ejemplo Sistemas de Gestion de Empleados.py',
        # SEMANA 7
        '10': 'UNIDAD 2/2.1 Constructores y Destructores/2.2.1-1 Uso de Constructores y Destructores.py',
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\n***************Menu Principal - Dashboard***************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()