# SEMANA 16
'''Desarrollar una aplicación GUI que permita a los usuarios gestionar una lista de tareas pendientes. La aplicación deberá permitir añadir nuevas tareas, marcar tareas como completadas, y eliminar tareas utilizando tanto la interfaz gráfica (clics de botón) como atajos de teclado.'''

import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x500")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada de tareas
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        # Lista de tareas (Listbox) 
        self.List_box = tk.Listbox(self.root, bg="#F0F8FF", fg="#000000", selectbackground="#4682B4", selectforeground="#FFFFFF")
        self.List_box.pack(pady=10)

        # Botones 
        self.add_button = tk.Button(self.root, text="Añadir tarea", command=self.add_task, bg="#32CD32", fg="white")
        self.add_button.pack(pady=10)
        
        self.complete_button = tk.Button(self.root, text="Marcar como completada", command=self.complete_task, bg="#1E90FF", fg="white")
        self.complete_button.pack(pady=10)
        
        self.delete_button = tk.Button(self.root, text="Eliminar tarea", command=self.delete_task, bg="#FF4500", fg="white")
        self.delete_button.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())  # Enter para añadir tarea
        self.root.bind("<c>", lambda event: self.complete_task())  # "C" para completar tarea
        self.root.bind("<d>", lambda event: self.delete_task())  # "D" para eliminar tarea
        self.root.bind("<Delete>", lambda event: self.delete_task())  # Tecla "Delete" para eliminar tarea
        self.root.bind("<Escape>", lambda event: self.root.quit())  # "Escape" para cerrar la aplicación

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  # Limpia el campo de entrada después de añadir la tarea
        else:
            messagebox.showerror("Error", "Por favor ingrese una tarea")

    def complete_task(self):
        """Marca la tarea seleccionada como completada."""
        selected_task_index = self.List_box.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.update_task_listbox()
        else:
            messagebox.showerror("Error", "Por favor seleccione una tarea")

    def delete_task(self):
        """Elimina la tarea seleccionada."""
        selected_task_index = self.List_box.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showerror("Error", "Por favor seleccione una tarea")
    
    def update_task_listbox(self):
        """Actualiza el Listbox mostrando las tareas pendientes y completadas con colores."""
        self.List_box.delete(0, tk.END)
        # Añadir tareas al Listbox con colores diferentes para completadas y pendientes
        for index, task in enumerate(self.tasks):
            display_task = task["task"]
            if task["completed"]:
                display_task += " (Completada)"
                self.List_box.insert(tk.END, display_task)
                self.List_box.itemconfig(index, {'fg': '#696969'})  # Tareas completadas en gris
            else:
                self.List_box.insert(tk.END, display_task)
                self.List_box.itemconfig(index, {'fg': '#000000'})  # Tareas pendientes en negro

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()