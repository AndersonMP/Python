from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

def imprimir_informe(laptop):
    informe = laptop.realizar_informe_uso()
    for clave,valor in informe.items():
        print(F"{clave} : {valor}")
    print("\n")

laptpop_jhon = Laptop("Lenovo", "Intel corei-5", 32)
laptpop_ana = Laptop("Lenovo", "Intel corei-5", 32, 600)

laptpop_mery = Laptop_Gaming("MSI", "i7", 4, "RTX-3090",500, 20)

laptop_melissa = Laptop_Business("HP", "Ryzen 5", 6, "32", "5", 800, 15)

# print(laptpop_jhon.__dict__)
# print(laptpop_jhon.valor_final())
# print(F"EL valor de descuento: {laptpop_jhon.valor_descuento(10)}")

# for numero in range(1, 1001):
#     asus_laptop = Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)


# print(Laptop.comparar_costo(laptpop_jhon, laptpop_ana))

print(laptpop_mery.realizar_diagnostico())
print(laptop_melissa.realizar_diagnositco())

print("Mery")
imprimir_informe(laptpop_mery)
print("Jhon")
imprimir_informe(laptpop_jhon)