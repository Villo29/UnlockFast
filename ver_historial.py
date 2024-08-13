import tkinter as tk
from tkinter import messagebox, ttk
import requests
from datetime import datetime

def ver_historial(root):
    # Crear una nueva ventana
    ventana_historial = tk.Toplevel()
    ventana_historial.title("Ver Historial")
    ventana_historial.geometry("400x500")
    ventana_historial.resizable(False,False)

    # Etiqueta y campo para la fecha
    tk.Label(ventana_historial, text="Seleccione la fecha (AÑO-MES-DIA)").pack(pady=5)
    entrada_fecha = tk.Entry(ventana_historial)
    entrada_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
    entrada_fecha.pack(pady=5)

    # Área de texto para mostrar los resultados
    resultado_texto = tk.Text(ventana_historial, wrap="word", height=15, width=50)
    resultado_texto.pack(pady=10)

    # Etiqueta para mostrar el total
    total_label = tk.Label(ventana_historial, text="Corte del día: ")
    total_label.pack(pady=5)

    # Función para manejar la búsqueda por fecha
    def buscar_por_fecha():
        fecha = entrada_fecha.get()

        try:
            response = requests.get(f"http://127.0.0.1:5000/historial?fecha={fecha}")
            response.raise_for_status()
            datos = response.json()

            if "error" in datos:
                messagebox.showerror("Error", datos["error"])
            else:
                resultado_texto.delete(1.0, tk.END)  # Limpiar el área de texto
                total = 0  # Variable para almacenar la suma de los precios
                for producto in datos:
                    resultado_texto.insert(tk.END, f"Precio: {producto['precio']}\n")
                    resultado_texto.insert(tk.END, f"Local: {producto['local']}\n")
                    resultado_texto.insert(tk.END, f"Fecha: {producto['fecha']}\n")
                    resultado_texto.insert(tk.END, "-"*40 + "\n")
                    resultado_texto.tag_configure("font", font=("Arial", 15))  # Set the font size
                    resultado_texto.tag_add("font", "1.0", "end")
                    total += int(producto['precio'])  # Convertir a entero y sumar el precio al total

                total_label.config(text=f"Corte del día: {total}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")

    # Botón para buscar
    btn_buscar = tk.Button(ventana_historial, text="Buscar", command=buscar_por_fecha)
    btn_buscar.pack(pady=10)

    def cerrar_ventana():
        ventana_historial.destroy()
        root.deiconify()

    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana_historial, text="Cerrar", command=cerrar_ventana)
    btn_cerrar.pack(pady=10)
