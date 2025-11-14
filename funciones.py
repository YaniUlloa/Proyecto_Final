import csv

gestor_reservas = []

def gestionar_reserva():
    rut = input("Ingrese rut del cliente: ").strip()
    for i in gestor_reservas:
        if i["rut"] == rut:
            print("Ya existe ese rut")
            return
    
    nombre = input("Ingrese nombre del cliente: ")
    fecha = input("Ingrese fecha de la reserva (dd/mm/aa): ")
    cabaña = input("Ingrese número de la cabaña: ")

    while True:
        try:
            cant_personas = input("Ingrese cantidad de personas: ")
            break
        except ValueError:
            print("Debes ingresar un valor numérico.")
    reserva = {
        "rut": rut,
        "nombre": nombre,
        "fecha": fecha,
        "cabaña": cabaña,
        "cant_personas": int(cant_personas)
    }

    gestor_reservas.append(reserva)
    print("Reserva ingresada con éxito!! ")

def lista_reserva():
    if not gestor_reservas:
        print("No hay reservas")
        return
    print("\nListado de reservas:")
    for a in gestor_reservas:
        print(f"{a["rut"]} | {a["nombre"]} | {a["fecha"]} | cabaña: {a["cabaña"]} | N° Personas:{a["cant_personas"]}")

def buscar_rut():
    rut= input("Ingresa el rut a buscar: ").strip()
    for i in gestor_reservas: 
        if i["rut"] == rut:
            print(f"Reserva encontrada {i}")
            return
    print("No se encontro una reserva.")

def actualizar_reserva():
    rut= input("Ingresa el rut para actualizar reserva: ").strip()
    for i in gestor_reservas:
        if i["rut"] == rut:
            print(f"Editar la reserva de {i["nombre"]}")
            i["fecha"] = input(f"Nueva fecha {i["fecha"]}: ") or i["fecha"]
            i["cabaña"] = input(f"Nueva cabaña {i["cabaña"]}: ") or i["cabaña"]
            nueva_cant = input(f"Nueva cantidad de personas (actual {i["cant_personas"]}: ") or i["cant_personas"]
            i["cant_personas"] = int(nueva_cant)
            print("Reserva actualizada")
            return
    print("No se encuentra el rut")

def eliminar_reserva():
    rut= input("Ingresa el rut que desea eliminar: ").strip()
    for i in gestor_reservas:
        if i["rut"] == rut:
            gestor_reservas.remove(i)
            print("Reserva eliminada con éxito.")
            return
    print("el rut no se encontró.")
