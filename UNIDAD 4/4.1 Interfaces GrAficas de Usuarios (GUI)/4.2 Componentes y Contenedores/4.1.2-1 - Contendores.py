import tkinter as tk 
from tkinter import ttk, messagebox 
from datetime import date 
import dateutil.utils 
from tkcalendar import DateEntry

# Crear la ventana principal
root = tk.Tk() # Crear la ventana principal
root.title("Contenedores") # Título de la ventana
root.geometry("800x600") # Tamaño de la ventana
root.configure(bg='#e6f7ff')  # Color de fondo de la ventana

# Crear un contenedor Frame
frame = ttk.Frame(root, padding="18")
frame.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW) # Posición del contenedor

# Agregar funciones
# Agregar el evento
def agregar_evento():
    nombre = nombre_entry.get() # Obtener el nombre del evento
    fecha = date_picker.get() # Obtener la fecha del evento
    hora = hora_entry.get() # Obtener la hora del evento
    descripcion = descripcion_entry.get() # Obtener la descripción del evento

    if nombre and fecha and hora and descripcion: # Verificar que todos los campos estén llenos
        tree.insert("", "end", values=(nombre, fecha, hora, descripcion)) # Agregar el evento a la tabla
        limpiar_campos() # Limpiar los campos
    else: 
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")

# Limpiar los campos después de agregar un evento
def limpiar_campos():
    nombre_entry.delete(0, tk.END) # Limpiar el campo de nombre
    hora_entry.delete(0, tk.END) # Limpiar el campo de hora
    descripcion_entry.delete(0, tk.END) # Limpiar el campo de descripción

# Función de eliminar el evento
def eliminar_evento():
    selected_item = tree.selection() # Obtener la selección del evento
    if selected_item: # Verificar que haya selección
        confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar el evento?")
        if confirmacion:
            tree.delete(selected_item) # Eliminar el evento de la tabla
    else:
        messagebox.showwarning("Eliminar", "No se ha seleccionado ningún evento para eliminar")

# Crear Título
titulo = ttk.Label(frame, text="Agenda Personal", font=("Arial", 24), foreground="#0059b3") 
titulo.grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.NSEW) # Posición del título

# Crear etiqueta y el campo de fecha
fecha_label = ttk.Label(frame, text="Fecha del evento:", foreground="#004d80") 
fecha_label.grid(row=1, column=0, pady=5, sticky=tk.W)
date_picker = DateEntry(frame, date_pattern="dd-mm-yyyy", width=12, background='#0059b3', foreground='white')
date_picker.set_date(date.today()) # Establecer la fecha actual como fecha predeterminada
date_picker.grid(row=1, column=1, pady=5, sticky=tk.W) # Posición del campo de fecha

# Campo para el nombre
nombre_label = ttk.Label(frame, text="Nombre del evento:", foreground="#004d80") # Crear etiqueta
nombre_label.grid(row=2, column=0, pady=5, sticky=tk.W) # Posición de la etiqueta
nombre_entry = ttk.Entry(frame) # Crear el campo de entrada
nombre_entry.grid(row=2, column=1, pady=5, sticky=tk.W) # Posición del campo de entrada

# Campo para la hora
hora_label = ttk.Label(frame, text="Hora del evento:", foreground="#004d80") # Crear etiqueta
hora_label.grid(row=3, column=0, pady=5, sticky=tk.W) # Posición de la etiqueta
hora_entry = ttk.Entry(frame)
hora_entry.grid(row=3, column=1, pady=5, sticky=tk.W) # Posición del campo de entrada

# Realizar la descripcion
descripcion_label = ttk.Label(frame, text="Descripción:", foreground="#004d80") 
descripcion_label.grid(row=4, column=0, pady=5, sticky=tk.W)
descripcion_entry = ttk.Entry(frame)
descripcion_entry.grid(row=4, column=1, pady=5, sticky=tk.W) # Posición del campo de entrada

# Crear botones
# Botón para agregar
boton_agregar = ttk.Button(frame, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=5, column=0, pady=10, sticky=tk.W) # Posición del botón agregar

# Botón para eliminar
boton_eliminar = ttk.Button(frame, text="Eliminar Evento", command=eliminar_evento)
boton_eliminar.grid(row=5, column=1, pady=10, sticky=tk.W) # Posición del botón eliminar

# Botón para salir
boton_salir = ttk.Button(frame, text="Salir", command=root.quit)
boton_salir.grid(row=5, column=1, pady=10, sticky=tk.E) # Posición del botón salir

# Crear el Treeview para mostrar la lista de eventos
tree = ttk.Treeview(frame, columns=("Nombre", "Fecha", "Hora", "Descripcion"), show="headings")
tree.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=10) # Posición del Treeview

# Agregar encabezados a las columnas
tree.heading("Nombre", text="Nombre") # Encabezado de nombre
tree.heading("Fecha", text="Fecha") # Encabezado de fecha
tree.heading("Hora", text="Hora") # Encabezado de hora
tree.heading("Descripcion", text="Descripción") # Encabezado de descripción

# Ajustar el tamaño de las columnas
tree.column("Nombre", width=150) # Ancho de la columna Nombre
tree.column("Fecha", width=100) # Ancho de la columna Fecha
tree.column("Hora", width=100) # Ancho de la columna Hora
tree.column("Descripcion", width=300)

# Ejecutar la aplicación
root.mainloop()