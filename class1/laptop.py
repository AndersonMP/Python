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

laptpop_jhon = Laptop("Lenovo", "Intel corei-5", "32")

print(laptpop_jhon.__dict__)
print(laptpop_jhon.valor_final())
print(F"EL valor de descuento: {laptpop_jhon.valor_descuento(10)}")