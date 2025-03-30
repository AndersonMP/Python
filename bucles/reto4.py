datos = []  
cantidad = int(input("¿Cuántos datos deseas ingresar? "))

for _ in range(cantidad):
    entrada = input("Ingresa un dato: ")

    if entrada.isdigit():
        datos.append(int(entrada))
    elif entrada.replace('.', '', 1).isdigit():
        datos.append(float(entrada))
    else:
        datos.append(entrada)

print(f"Su lista es: {datos}")
