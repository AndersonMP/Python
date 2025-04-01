import random, json
from laptop import Laptop

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria,costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def realizar_diagnositco(self):
        resultado_diagnostico = super().realizar_diagnostico()
        resultado_diagnostico["Almacenamiento"] = self.almacenamiento
        resultado_diagnostico["Duración de Batería"] = self.duracion_bateria
        resultado_diagnostico["Resultado Conectividad Red"] = self.verificar_conectividad_red()
        return json.dumps(resultado_diagnostico, indent=4, ensure_ascii=False)

    def verificar_conectividad_red(self):
        conectividad_red = ["disponibilidad_wifi", "acceso_servidores_empresariales", "latencia"]
        resultados = {}
        
        for red in conectividad_red:
            resultados[red] = random.choice([True, False])
        
        return resultados

