# =====================================================
# CLASE MASCOTA
# Sistema de gestión de mascotas usando POO
# =====================================================

class Mascota:

    # Constructor
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    # Método para mostrar información
    def mostrar_informacion(self):
        print("\n===== INFORMACIÓN DE LA MASCOTA =====")
        print("Nombre :", self.nombre)
        print("Especie:", self.especie)
        print("Edad   :", self.edad, "años")

    # Método para emitir un sonido
    def hacer_sonido(self):
        # CORRECCIÓN: Se alinearon correctamente estas listas con el flujo del método
        perros = [
            "perro",
            "pomerania",
            "labrador",
            "pastor aleman",
            "chihuahua"
        ]

        gatos = [
            "gato",
            "siames",
            "persa"
        ]

        if self.especie.lower() in perros:
            print(self.nombre, "dice: ¡Guau Guau!")

        elif self.especie.lower() in gatos:
            print(self.nombre, "dice: ¡Miau!")

        elif self.especie.lower() == "loro":
            print(self.nombre, "dice: ¡Hola!")

        else:
            print(self.nombre, "emite un sonido característico.")

    # Método principal para registrar y ejecutar
    def ejecutar(self):
        print("=== REGISTRO DE MASCOTAS ===")

        print("\nMascota 1")
        nombre1 = input("Ingrese el nombre: ")
        especie1 = input("Ingrese la especie: ")
        edad1 = int(input("Ingrese la edad: "))

        mascota1 = Mascota(nombre1, especie1, edad1)

        print("\nMascota 2")
        nombre2 = input("Ingrese el nombre: ")
        especie2 = input("Ingrese la especie: ")
        edad2 = int(input("Ingrese la edad: "))

        mascota2 = Mascota(nombre2, especie2, edad2)

        mascota1.mostrar_informacion()
        mascota1.hacer_sonido()

        mascota2.mostrar_informacion()
        mascota2.hacer_sonido()
        