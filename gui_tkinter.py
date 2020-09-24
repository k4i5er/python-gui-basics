from tkinter import *  # Esta es la forma básica de importación
from tkinter import ttk  # Importamos los elementos nuevos de tkinter

txt = "Texto desde variable"
# Definimos la ventana principal de nuestra app
root = Tk()  # Instancia (derivación/hijo) de Tk()

# Definimos una ventana de 800px de ancho x 600px de alto
root.geometry('800x600')

# Definimos un título para nuestra ventana
root.title('Mi primer ventana en Python')

# Cambiar color de fondo a la ventana
root.configure(bg='#1d1990')

# Agregamos una etiqueta
ttk.Label(root, text=txt).pack(side=TOP)

miVariable = ""
# Agregamos una caja de texto
ttk.Entry(root, textvariable=miVariable, width=20).pack(side=TOP)

# Agregamos un widget botón para salir del programa
ttk.Button(root, text="Cerrar ventana", command=quit).pack(side=BOTTOM)

# Representa la ventana en pantalla
root.mainloop()
