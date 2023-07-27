import tkinter as tk
import random

def cambiar_color():
    # Generar colores RGB aleatorios
    color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # Cambiar el color de fondo de la etiqueta
    etiqueta.config(bg=color)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Hola Mundo con animaciones")
ventana.geometry("400x200")

# Crear una etiqueta con el mensaje "Hola Mundo"
etiqueta = tk.Label(ventana, text="Hola Mundo", font=("Arial", 24))
etiqueta.pack(pady=50)

# Crear un botón que cambia el color al hacer clic
boton_cambiar_color = tk.Button(ventana, text="Cambiar Color", command=cambiar_color)
boton_cambiar_color.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
