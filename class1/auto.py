from datetime import datetime
class Auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def actualizar_kilometraje(self, kilometraje):
        if kilometraje < self.kilometraje:
            print("No se puede reducir el kilometraje.")
            exit()
        elif kilometraje < 0:
            print("El kilometraje no puede ser negativo.")
            exit()
        
        self.kilometraje = kilometraje
        return f"Kilometraje actualizado a {self.kilometraje} km."

    def realizar_viaje(self, kilometros):
        if kilometros < 0:
            print("La cantidad de kilómetros debe ser positiva.")
            exit()       
        self.kilometraje += kilometros
        return f"Viaje realizado. Kilometraje actual: {self.kilometraje} km."

    def estado_auto(self):
        if self.kilometraje < 20000:
            return "Estoy como nuevo."
        elif 20000 <= self.kilometraje <= 100000:
            return "Ya estoy usado."
        else:
            return "¡Ya déjame descansar por favor!"

    def mostrar_informacion(self):
        return f"{self.marca} {self.modelo} ({self.año}) - {self.kilometraje} km"
    
    @classmethod
    def crear_auto(cls):
        marca = "Toyota"
        modelo = "Hilux"
        año = 2025
        return cls(marca, modelo, año)
    
    @classmethod
    def crear_con_diccionario(cls, datos):
        return cls(datos['marca'], datos['modelo'], datos['año'], datos.get('kilometraje', 0))

    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Tienen el mismo kilometraje"
        return "Tienen distinto kilometraje"
    
    @staticmethod
    def antiguedad_auto(auto):
        antiguedad = datetime.now().year - auto.año
        return antiguedad

# Crear una instancia de Auto
auto1 = Auto("BMW", "Sedán", 2005)

kilometraje = int(input("Ingrese el kilometraje: "))
print(auto1.actualizar_kilometraje(kilometraje))  

km_viaje = int(input("Ingrese kilómetros del viaje: "))
print(auto1.realizar_viaje(km_viaje))

print(auto1.mostrar_informacion())
print(auto1.estado_auto())

toyota = Auto.crear_auto()
print(toyota.__dict__)

print(Auto.comparar_kilometraje(toyota, auto1))
datos_auto = {"marca": "Ford", "modelo": "Focus", "año": 2018, "kilometraje": 45000}
auto2 = Auto.crear_con_diccionario(datos_auto)
print(auto2.mostrar_informacion())


print(f"Antigüedad del auto 1: {Auto.antiguedad_auto(auto1)} años")
print(f"Antigüedad del auto 2: {Auto.antiguedad_auto(auto2)} años")