import tkinter as tk
from datetime import datetime
import requests
from tkinter import messagebox

def agregar_producto(root):
    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar Producto")
    ventana_agregar.geometry("300x400")
    ventana_agregar.resizable(False, False)

    tk.Label(ventana_agregar, text="Precio:", width=30,
            anchor='w', font=("bold", 14)).pack(pady=5)
    entrada_precio = tk.Entry(ventana_agregar, width=30, font=("Arial", 12))
    entrada_precio.pack(pady=5)

    tk.Label(ventana_agregar, text="Local:", width=30,
            anchor='w', font=("bold", 14)).pack(pady=5)
    entrada_local = tk.Entry(ventana_agregar, width=30)
    entrada_local.pack(pady=5)

    tk.Label(ventana_agregar, text="Fecha:", width=30,
            anchor='w', font=("bold", 14)).pack(pady=5)
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    entrada_fecha = tk.Entry(ventana_agregar)
    entrada_fecha.insert(0, fecha_actual)
    entrada_fecha.pack(pady=5)

    def enviar_datos():
        precio = entrada_precio.get()
        local = entrada_local.get()
        fecha = entrada_fecha.get()

        data = {
            "precio": precio,
            "local": local,
            "fecha": fecha
        }

        try:
            response = requests.post(
                "http://127.0.0.1:5000/agregar", json=data)
            response.raise_for_status()
            messagebox.showinfo("Éxito", "Producto agregado exitosamente")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al enviar datos: {e}")

        ventana_agregar.destroy()
        root.deiconify()

    btn_enviar = tk.Button(
        ventana_agregar, text="Enviar", command=enviar_datos)
    btn_enviar.pack(pady=10)

    def cerrar_ventana():
        ventana_agregar.destroy()
        root.deiconify()

    btn_cerrar = tk.Button(ventana_agregar, text="Cerrar", command=cerrar_ventana)
    btn_cerrar.pack(pady=10)