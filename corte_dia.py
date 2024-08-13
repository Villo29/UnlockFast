import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

def corte_dia(root):
    ventana_corte = tk.Toplevel(root)
    ventana_corte.title("Corte del Día")
    ventana_corte.geometry("240x400")
    ventana_corte.resizable(False,False)

    tk.Label(ventana_corte, text="Seleccione la fecha (AÑO-MES-DIA)").pack(pady=5)
    entrada_fecha = tk.Entry(ventana_corte)
    entrada_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
    entrada_fecha.pack(pady=5)

    resultado_label = tk.Label(ventana_corte, text="", font=("Arial", 14))
    resultado_label.pack(pady=20)

    def obtener_corte():
        fecha = entrada_fecha.get()
        try:
            response = requests.get(f"http://127.0.0.1:5000/corte_dia?fecha={fecha}")
            response.raise_for_status()
            datos = response.json()
            if "error" in datos:
                messagebox.showerror("Error", datos["error"])
            else:
                total = datos["total"]
                resultado_label.config(text=f"Total del día: ${total}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")

    btn_calcular = tk.Button(ventana_corte, text="Calcular", command=obtener_corte)
    btn_calcular.pack(pady=10)

    def cerrar_ventana():
        ventana_corte.destroy()
        root.deiconify()

    btn_cerrar = tk.Button(ventana_corte, text="Cerrar", command=cerrar_ventana)
    btn_cerrar.pack(pady=10)
