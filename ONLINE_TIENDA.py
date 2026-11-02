import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os

ARCHIVO = "productos.json"

def cargar_productos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_productos():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(productos, f, indent=4, ensure_ascii=False)

def agregar_producto():
    nombre = entry_nombre.get()
    descripcion = txt_descripcion.get("1.0", tk.END).strip()
    precio = entry_precio.get()

    if not nombre or not precio:
        messagebox.showerror("Error", "Complete nombre y precio.")
        return

    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "fotos": fotos_actuales.copy()
    }

    productos.append(producto)
    guardar_productos()
    actualizar_lista()

    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    txt_descripcion.delete("1.0", tk.END)

    fotos_actuales.clear()
    lbl_fotos.config(text="0 fotos cargadas")

    messagebox.showinfo("Éxito", "Producto agregado.")

def seleccionar_fotos():
    global fotos_actuales

    archivos = filedialog.askopenfilenames(
        title="Seleccionar fotos",
        filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.webp")]
    )

    fotos_actuales = list(archivos[:5])

    lbl_fotos.config(text=f"{len(fotos_actuales)} fotos cargadas")

def actualizar_lista():
    lista.delete(0, tk.END)

    for p in productos:
        lista.insert(
            tk.END,
            f"{p['nombre']} - $ {p['precio']}"
        )

def ver_producto(event):
    seleccion = lista.curselection()

    if not seleccion:
        return

    indice = seleccion[0]
    p = productos[indice]

    texto = f"""
Nombre: {p['nombre']}

Precio: $ {p['precio']}

Descripción:
{p['descripcion']}

Fotos:
"""

    for foto in p["fotos"]:
        texto += f"\n{foto}"

    detalle.delete("1.0", tk.END)
    detalle.insert(tk.END, texto)

# ------------------------
# Ventana principal
# ------------------------

root = tk.Tk()
root.title("TIENDA ONLINE")
root.geometry("900x600")

productos = cargar_productos()
fotos_actuales = []

frame_izq = tk.Frame(root)
frame_izq.pack(side="left", fill="both", expand=True, padx=10, pady=10)

frame_der = tk.Frame(root)
frame_der.pack(side="right", fill="both", expand=True, padx=10, pady=10)

tk.Label(frame_izq, text="Nombre").pack()
entry_nombre = tk.Entry(frame_izq, width=40)
entry_nombre.pack()

tk.Label(frame_izq, text="Precio").pack()
entry_precio = tk.Entry(frame_izq, width=40)
entry_precio.pack()

tk.Label(frame_izq, text="Descripción").pack()

txt_descripcion = tk.Text(frame_izq, height=8, width=40)
txt_descripcion.pack()

tk.Button(
    frame_izq,
    text="Cargar hasta 5 fotos",
    command=seleccionar_fotos
).pack(pady=5)

lbl_fotos = tk.Label(frame_izq, text="0 fotos cargadas")
lbl_fotos.pack()

tk.Button(
    frame_izq,
    text="Agregar producto",
    bg="green",
    fg="white",
    command=agregar_producto
).pack(pady=10)

tk.Label(
    frame_der,
    text="Catálogo"
).pack()

lista = tk.Listbox(frame_der, width=40)
lista.pack(fill="both", expand=True)

lista.bind("<<ListboxSelect>>", ver_producto)

detalle = tk.Text(frame_der, height=15)
detalle.pack(fill="both", expand=True)

actualizar_lista()

root.mainloop()