planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
gravedad_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_bus = 1213

# print(planetas[8])

print(F"En la Tierra, un autobús de dos pisos pesa {peso_bus} N")
print(F"En Mercurio, un autobús de dos pisos pesa {peso_bus * gravedad_planetas[0]} N")

print(F"Lo más liviano que sería un autobús en el sistema solar es {peso_bus * min(gravedad_planetas)} N")
print(F"Lo más pesado que sería un autobús en el sistema solar es {peso_bus * max(gravedad_planetas)} N")
