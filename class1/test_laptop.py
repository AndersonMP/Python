from laptop import Laptop;


laptpop_jhon = Laptop("Lenovo", "Intel corei-5", "32")
laptpop_ana = Laptop("Lenovo", "Intel corei-5", "32", 600)


# print(laptpop_jhon.__dict__)
# print(laptpop_jhon.valor_final())
# print(F"EL valor de descuento: {laptpop_jhon.valor_descuento(10)}")

for numero in range(1, 1001):
    asus_laptop = Laptop.asus_laptop(numero)
    print(asus_laptop.__dict__)


# print(Laptop.comparar_costo(laptpop_jhon, laptpop_ana))

