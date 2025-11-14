import csv
from funciones import gestor_reservas

def guardar_csv(nombre_archivo="reservas.csv"):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["rut", "nombre", "fecha", "cabaña", "cant_personas"])
        escritor.writeheader()
        escritor.writerows(gestor_reservas)
    print("Archivo guardado correctamente.")

def cargar_csv(nombre_archivo="reservas.csv"):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            gestor_reservas.clear()
            for fila in lector:
                fila["cant_personas"] = int(fila["cant_personas"])
                gestor_reservas.append(fila)
        print("Datos cargados exitosamente.")
    except FileNotFoundError:
        print("No existe archivo CSV, se creará al guardar.")

