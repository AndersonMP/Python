from laptop import Laptop;

class Laptop_Gaming(Laptop):
    def __init__(self, marca, procesador, memoria, tarj_graf, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto) 
        self.tarj_graf = tarj_graf

    def realizar_diagnostico(self):
        resultado_diagnostico = super().realizar_diagnostico()
        resultado_juegos = self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultado juegos"] = resultado_juegos
        return resultado_diagnostico
    
    def realizar_diagnostico_juegos(self):
        juegos = ["FORTNITE", "COD", "GTA"]
        resultados = {}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarj_graf:
                fps = fps_base * 3
            elif "GTX" in self.tarj_graf:
                fps = fps_base * 2
            else:
                fps = fps_base
        
        resultados[juego] = F"{fps} FPS"
        return resultados
    
