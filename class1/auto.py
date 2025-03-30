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
        return F"Kilometraje actualizado a {self.kilometraje} km."

    def realizar_viaje(self, kilometros):
        if kilometros < 0:
            print("La cantidad de kilómetros debe ser positiva.")
            exit()       
        self.kilometraje += kilometros
        return F"Viaje realizado. Kilometraje actual: {self.kilometraje} km."

    def estado_auto(self):
        if self.kilometraje < 20000:
            return "Estoy como nuevo."
        elif 20000 <= self.kilometraje <= 100000:
            return "Ya estoy usado."
        else:
            return "¡Ya déjame descansar por favor!"

    def mostrar_informacion(self):
        return "{self.marca} {self.modelo} ({self.año}) - {self.kilometraje} km"


# Crear una instancia de Auto
auto1 = Auto("BMW", "Sedán", 2005)

kilometraje = int(input("Ingrese el kilometraje: "))
print(auto1.actualizar_kilometraje(kilometraje))  

km_viaje = int(input("Ingrese kilómetros del viaje: "))
print(auto1.realizar_viaje(km_viaje))

print(auto1.mostrar_informacion())
print(auto1.estado_auto())
