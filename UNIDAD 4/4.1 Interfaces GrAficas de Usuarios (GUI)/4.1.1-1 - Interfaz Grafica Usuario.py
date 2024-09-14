# SEMANA 13
'''Desarrollar una aplicación de interfaz gráfica de usuario (GUI) que permita a los usuarios interactuar con datos de manera visual, utilizando los conceptos aprendidos sobre GUI.'''

import tkinter as tk

# Crear la ventana
app = tk.Tk()  # Crear la ventana
app.title("Interfaz Gráfica")  # Título de la ventana
app.geometry("600x800")  # Tamaño de la ventana
app.configure(bg="#2F3C7E")  # Color de fondo: azul oscuro

# Variables
entrada = tk.StringVar(app)
lista_datos = []

# Función de agregar datos
def agregar_datos():
    texto_ingresado = entrada.get()
    if texto_ingresado:
        lista.insert(tk.END, texto_ingresado)
        entrada.set("")
        mensaje.set("")  # Limpiar mensaje de error si se agrega el dato correctamente
    else:
        mensaje.set("Por favor, ingrese un dato.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)  # Borrar todos los elementos de la lista

# COMPONENTES
# Etiqueta
tk.Label(app, text="Ingrese el valor: ", font=("Arial", 12), bg="#FBEAEB", fg="#2F3C7E").pack(pady=12)  # Fondo rosa suave y texto azul oscuro

# Caja de texto
tk.Entry(app, fg="black", bg="#F6F7EB", font=("Arial", 12), textvariable=entrada).pack(pady=12)  # Fondo beige claro

# Mensaje de error
mensaje = tk.StringVar()
tk.Label(app, textvariable=mensaje, font=("Arial", 10), bg="#2F3C7E", fg="#FF5959").pack(pady=5)  # Texto rojo en fondo azul oscuro

# Crear botón "Agregar"
tk.Button(app, text="Agregar", font=("Arial", 12), bg="#00B8A9", fg="white", command=agregar_datos).pack(pady=12)  # Botón verde menta y texto blanco

# Lista para agregar datos
lista = tk.Listbox(app, font=("Arial", 12), width=40, height=20, bg="#F6F7EB", fg="#2F3C7E")
lista.pack(pady=12)  # Fondo beige claro con texto azul oscuro

# Crear botón "Limpiar"
tk.Button(app, text="Limpiar", font=("Arial", 12), bg="#FF5959", fg="white", command=limpiar_lista).pack(pady=12)  # Botón rojo brillante y texto blanco

# Ejecutar el bucle principal de la aplicación
app.mainloop()
