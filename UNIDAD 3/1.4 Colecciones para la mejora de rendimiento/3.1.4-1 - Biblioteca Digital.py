# SEMANA 12
# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn): # Constructor
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.informacion = (titulo, autor) # Información del libro

    def __str__(self): # Método para imprimir la información del libro
        return f"ISBN: {self.isbn}\nTítulo: {self.titulo}\nAutor: {self.autor}\nCategoría: {self.categoria}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario): # Constructor
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados al usuario


# Clase Biblioteca
class Biblioteca:
    def __init__(self): # Constructor
        self.libros = {}  # Diccionario con los libros disponibles (clave: ISBN)
        self.usuarios = {}  # Diccionario con los usuarios (clave: ID de usuario)
        self.ids_usuario = set()  # Conjunto para IDs de usuarios únicos

    # Funcionalidades
    # Agregar Libro
    def agregar_libro(self, libro): # Agregar libro a la biblioteca
        if libro.isbn in self.libros: 
            print(f'El libro {libro.titulo} ya existe en la biblioteca.')
        else:
            self.libros[libro.isbn] = libro
            print(f'El libro {libro.titulo} ha sido agregado a la biblioteca.')

    # Quitar Libro
    def quitar_libro(self, isbn): # Quitar libro de la biblioteca
        if isbn in self.libros:
            del self.libros[isbn] # Eliminar el libro del diccionario
            print(f'El libro con ISBN {isbn} ha sido eliminado de la biblioteca.')
        else:
            print(f'El libro con ISBN {isbn} no existe en la biblioteca.')

    # Agregar Usuario
    def agregar_usuario(self, usuario): # Agregar usuario a la biblioteca
        if usuario.id_usuario in self.usuarios:
            print(f'El usuario {usuario.id_usuario} ya existe en la biblioteca.')
        else:
            self.usuarios[usuario.id_usuario] = usuario # Agregar usuario al diccionario
            self.ids_usuario.add(usuario.id_usuario)
            print(f'El usuario {usuario.id_usuario} ha sido agregado a la biblioteca.')

    # Dar de baja al usuario
    def dar_baja_usuario(self, id_usuario): # Dar de baja al usuario
        if id_usuario in self.ids_usuario:
            del self.usuarios[id_usuario] # Eliminar el usuario del diccionario
            self.ids_usuario.remove(id_usuario)
            print(f'El usuario {id_usuario} ha sido dado de baja de la biblioteca.')
        else:
            print(f'El usuario {id_usuario} no existe en la biblioteca.')

    # Prestar libro
    def prestar_libro(self, id_usuario, isbn): # Prestar libro al usuario
        if id_usuario not in self.usuarios: # Verificar si el usuario existe
            print(f'El usuario {id_usuario} no existe en la biblioteca.')
        elif isbn not in self.libros: # Verificar si el libro existe
            print(f'El libro con ISBN {isbn} no existe en la biblioteca.')
        else:
            usuario = self.usuarios[id_usuario] 
            libro = self.libros[isbn]
            if libro in usuario.libros_prestados: # Verificar si el libro ya está prestado
                print(f'El libro {libro.titulo} ya ha sido prestado a {usuario.nombre}.')
            else:
                usuario.libros_prestados.append(libro) # Agregar el libro a la lista de libros prestados
                del self.libros[isbn]  # Quitar el libro de la biblioteca
                print(f'El libro {libro.titulo} ha sido prestado a {usuario.nombre}.')

    # Devolver libro
    def devolver_libro(self, id_usuario, isbn): # Devolver libro al usuario
        if id_usuario not in self.usuarios: # Verificar si el usuario existe
            print(f'El usuario {id_usuario} no existe en la biblioteca.')
        else:
            usuario = self.usuarios[id_usuario]
            libro_prestado = None
            for libro in usuario.libros_prestados: # Buscar el libro prestado
                if libro.isbn == isbn:
                    libro_prestado = libro
                    break
            if libro_prestado:
                usuario.libros_prestados.remove(libro_prestado) # Eliminar el libro de la lista de libros prestados
                self.libros[isbn] = libro_prestado  # Devolver el libro a la biblioteca
                print(f'El libro {libro_prestado.titulo} ha sido devuelto a la biblioteca.')
            else:
                print(f'El libro con ISBN {isbn} no ha sido prestado a {usuario.nombre}.')

    # Buscar libro por título, autor o categoría
    def buscar_libro(self, busqueda): 
        resultados = []
        for libro in self.libros.values(): # Recorrer todos los libros en la biblioteca
            if (busqueda.lower() in libro.titulo.lower() or
                busqueda.lower() in libro.autor.lower() or
                busqueda.lower() in libro.categoria.lower()): # Verificar si la búsqueda coincide con el título, autor o categoría del libro
                resultados.append(libro) 
        if resultados:
            print(f'Se encontraron {len(resultados)} libros que coinciden con la búsqueda:')
            for libro in resultados: # Imprimir los resultados de la búsqueda
                print(libro)
        else:
            print('No se encontraron libros que coincidan con la búsqueda.')

    # Mostrar una lista de todos los libros actualmente prestados a un usuario.
    def listar_libros_prestados(self, id_usuario): 
        if id_usuario in self.usuarios: # Verificar si el usuario existe
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados: # Verificar si el usuario tiene libros prestados
                print(f'Libros prestados a {usuario.nombre}:')
                for libro in usuario.libros_prestados: # Imprimir los libros prestados
                    print(libro)
            else:
                print(f'El usuario {usuario.nombre} no tiene libros prestados.')
        else:
            print(f'El usuario {id_usuario} no existe en la biblioteca.')


# Menú interactivo
def menu():
    mi_biblioteca = Biblioteca() # Crear una instancia de la clase Biblioteca
    while True: # Bucle infinito para mostrar el menú
        print('--- Menú Biblioteca ---') # Imprimir el menú
        print('1. Agregar libro') 
        print('2. Quitar libro')
        print('3. Agregar usuario')
        print('4. Dar de baja usuario')
        print('5. Prestar libro')
        print('6. Devolver libro')
        print('7. Buscar libro')
        print('8. Listar libros prestados')
        print('9. Salir')
        opcion = input('Seleccione una opción: ') # Pedir al usuario que seleccione una opción

        if opcion == '1': # Opción 1: Agregar libro
            titulo = input('Ingrese el título del libro: ')
            autor = input('Ingrese el autor del libro: ')
            categoria = input('Ingrese la categoría del libro: ')
            isbn = input('Ingrese el ISBN del libro: ')
            libro = Libro(titulo, autor, categoria, isbn)
            mi_biblioteca.agregar_libro(libro)

        elif opcion == '2': # Opción 2: Quitar libro
            isbn = input('Ingrese el ISBN del libro que desea quitar: ')
            mi_biblioteca.quitar_libro(isbn)

        elif opcion == '3': # Opción 3: Agregar usuario
            nombre = input('Ingrese el nombre del usuario: ')
            id_usuario = input('Ingrese el ID del usuario: ')
            usuario = Usuario(nombre, id_usuario)
            mi_biblioteca.agregar_usuario(usuario)

        elif opcion == '4': # Opción 4: Dar de baja usuario
            id_usuario = input('Ingrese el ID del usuario que desea dar de baja: ')
            mi_biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == '5': # Opción 5: Prestar libro
            id_usuario = input('Ingrese el ID del usuario que desea prestar el libro: ')
            isbn = input('Ingrese el ISBN del libro que desea prestar: ')
            mi_biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == '6': # Opción 6: Devolver libro
            id_usuario = input('Ingrese el ID del usuario que desea devolver el libro: ')
            isbn = input('Ingrese el ISBN del libro que desea devolver: ')
            mi_biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == '7': # Opción 7: Buscar libro
            busqueda = input('Ingrese el título, autor o categoría del libro que desea buscar: ')
            mi_biblioteca.buscar_libro(busqueda)

        elif opcion == '8': # Opción 8: Listar libros prestados
            id_usuario = input('Ingrese el ID del usuario que desea listar los libros prestados: ')
            mi_biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == '9': # Opción 9: Salir
            print('Gracias por usar la biblioteca.')
            break

        else: # Opción inválida
            print('Opción inválida, por favor seleccione una opción válida.')


menu() # Llamar a la función menu() para iniciar el programa

