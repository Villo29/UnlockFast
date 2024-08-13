import tkinter as tk
from agregar_producto import agregar_producto
from ver_historial import ver_historial
from corte_dia import corte_dia

class PuntoVenta:
    def __init__(self, master):
        self.master = master
        master.title("Puro UnlockFast ALV")
        master.geometry("300x400")
        master.resizable(False,False)

        self.btn_agregar = tk.Button(
            master, text="Agregar", command=lambda: self.abrir_submenu(agregar_producto, self.master))
        self.btn_agregar.pack(fill="x", padx=10, pady=10)

        self.btn_historial = tk.Button(
            master, text="Historial", command=lambda: self.abrir_submenu(ver_historial, self.master))
        self.btn_historial.pack(fill="x", padx=10, pady=10)

        self.btn_corte_dia = tk.Button(
            master, text="Corte de Día", command=lambda: self.abrir_submenu(corte_dia, self.master))
        self.btn_corte_dia.pack(fill="x", padx=10, pady=10)

        self.btn_cerrar = tk.Button(master, text="Cerrar", command=master.quit)
        self.btn_cerrar.pack(fill="x", padx=10, pady=10)

    def abrir_submenu(self, funcion, *args):
        self.master.withdraw()
        funcion(*args)

root = tk.Tk()
my_gui = PuntoVenta(root)
root.mainloop()