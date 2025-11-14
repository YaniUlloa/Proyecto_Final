import funciones as fn
from archivo import guardar_csv, cargar_csv

def menu():
    cargar_csv()

    while True:
        print("\n--- GESTOR DE RESERVAS REFUGIO ANDINO ---")
        print("1. Crear reserva")
        print("2. Listar reservas")
        print("3. Buscar por RUT")
        print("4. Actualizar reserva")
        print("5. Eliminar reserva")
        print("6. Guardar en CSV")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            fn.gestionar_reserva()
        elif opcion == "2":
            fn.lista_reserva()
        elif opcion == "3":
            fn.buscar_rut()
        elif opcion == "4":
            fn.actualizar_reserva()
        elif opcion == "5":
            fn.eliminar_reserva()
        elif opcion == "6":
            guardar_csv()
        elif opcion == "7":
            guardar_csv()
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
