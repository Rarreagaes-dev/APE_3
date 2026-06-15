# =====================================================
# PROGRAMA TRADICIONAL
# Sistema de gestión de mascotas
# Semana 3 - Programación Orientada a Objetos
# =====================================================

# Función para registrar una mascota
def registrar_mascota():

    print("\n=== REGISTRO DE MASCOTA ===")

    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))

    return nombre, especie, edad


# Función para mostrar la información de la mascota
def mostrar_mascota(nombre, especie, edad):

    print("\n===== INFORMACIÓN DE LA MASCOTA =====")
    print("Nombre :", nombre)
    print("Especie:", especie)
    print("Edad   :", edad, "años")


# Función principal del programa
def ejecutar():

    while True:

        print("\n========== MENÚ ==========")
        print("1. Registrar mascota")
        print("2. Salir")
        print("==========================")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            # Registrar mascota
            nombre, especie, edad = registrar_mascota()

            # Mostrar información
            mostrar_mascota(nombre, especie, edad)

        elif opcion == 2:

            print("\nGracias por utilizar el sistema.")
            break

        else:

            print("\nOpción no válida.")


# Inicio del programa
ejecutar()