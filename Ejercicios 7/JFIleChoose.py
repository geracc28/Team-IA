import os
from tkinter import Tk, filedialog

def seleccionar_archivo_o_directorio():
    Tk().withdraw()  # Evita que se abra la ventana principal de Tkinter
    ruta_inicial = "d:\\Documentos\\IMAGENES\\"
    ruta_seleccionada = filedialog.askopenfilename(initialdir=ruta_inicial,
                                                    title="Elegir",
                                                    filetypes=(("todos los archivos", "*.*"), ("archivos de texto", "*.txt")))
    if ruta_seleccionada:
        #mostrar_informacion(ruta_seleccionada)
        return ruta_seleccionada
    else:
        print("No se seleccionó ningún archivo o directorio.")

def mostrar_informacion(ruta):
    if os.path.isdir(ruta):
        tipo = "Carpeta"
        print(f"Elegiste: {ruta}")
        print(f"Tipo: {tipo}")
        print("Contenido:")
        for item in os.listdir(ruta):
            print(f" -> {item}")
    elif os.path.isfile(ruta):
        tipo = "Archivo"
        permisos = ""
        permisos += "r" if os.access(ruta, os.R_OK) else ""
        permisos += "w" if os.access(ruta, os.W_OK) else ""
        permisos += "x" if os.access(ruta, os.X_OK) else ""
        print(f"Elegiste: {ruta}")
        print(f"Tipo: {tipo}")
        print(f"Tamaño: {os.path.getsize(ruta)} bytes")
        print(f"Permisos: {permisos}")

# if __name__ == "__main__":
#     seleccionar_archivo_o_directorio()
