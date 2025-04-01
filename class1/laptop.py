import random;

class Laptop:
    def __init__(self, marca, procesador, memoria, costo = 500, impuesto = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto
    
    def valor_final(self):
        return self.costo + self.impuesto

    def valor_descuento(self, descuento):
        return (self.costo * descuento) / 100

    def realizar_diagnostico(self):
        resultado = {
            "MARCA": F"{self.marca}",
            "PROCESADOR": F"{self.procesador}",
            "MEMORIA RAM": "OK" if  self.memoria >= 8 else "Aumentar memoria RAM",
            "BATERÍA": "OK" if random.choice([True, False]) else "Cambiar de batería"
        }
        return resultado
    
    def realizar_informe_uso(self):
        resultado_informe = {
            "Tipo": "Genérica",
            "Uso Recomendado": "Tareas cotidianas",
            "Horas de uso": 5,
            "Diagnóstico actual": self.realizar_diagnostico()
        }
        return resultado_informe
    
    @staticmethod
    def comparar_costo(laptop1, laptop2):
        if laptop1.costo == laptop2.costo:
            return "Los costos son iguales"
        return "Los costos son diferentes"

    @classmethod
    def asus_laptop (cls, costo):
        marca = "asus"
        procesador = "i5"
        memoria = 16
        return cls(marca, procesador, memoria, costo)