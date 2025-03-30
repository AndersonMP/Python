import random

aleatorio = random.randint(1,9)
aleatorio_dos = random.randint(1,9)

if aleatorio == 4:
    print("Ganaste")
elif aleatorio == 8:
    print("Suerte")
elif aleatorio == 3 and aleatorio_dos == 7:
    print("Jackpot")
else:
    print("Perdiste")

