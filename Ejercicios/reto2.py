print("Seleccione un país:")
print("1. Colombia")
print("2. Ecuador")
print("3. Perú")
pais = int(input("Ingrese el número del país: "))

print("Seleccione la zona: ")
print("1. Urbana")
print("2. Rural")
print("3. Perimetral")
zona = int(input("Ingrese el número de zona: "))

velocidad = int(input("Ingrese la velocidad actual (km/h): "))

# Colombia
max_zona_urbana_co = 30
min_zona_urbana_co = 10
max_zona_rural_co = 80
min_zona_rural_co = 31
max_zona_perimetral_co = 100
min_zona_perimetral_co = 81

# Ecuador
max_zona_urbana_ec = 50
min_zona_urbana_ec = 10
max_zona_rural_ec = 70
min_zona_rural_ec = 51
max_zona_perimetral_ec = 90
min_zona_perimetral_ec = 71

# Perú
max_zona_urbana_pe = 40
min_zona_urbana_pe = 10
max_zona_rural_pe = 60
min_zona_rural_pe = 41
max_zona_perimetral_pe = 120
min_zona_perimetral_pe = 61

if pais == 1:
    if zona == 1:
        if velocidad >= min_zona_urbana_co and velocidad <= min_zona_urbana_co:
            print("Rango de velocidad permitido")
        else: 
            print("Fuera del límite de velocidad")  
    elif zona == 2:
        if velocidad >= min_zona_rural_co and velocidad <= min_zona_rural_co:
            print("Rango de velocidad permitido")
        else: 
            print("Fuera del límite de velocidad")  
    elif zona == 3:
        if velocidad >= min_zona_perimetral_co and velocidad <= min_zona_perimetral_co:
            print("Rango de velocidad permitido")
        else: 
            print("Fuera del límite de velocidad")  
    else:
        print("Zona no permitidad")
elif pais == 2:
    if zona == 1:
        if velocidad >= min_zona_urbana_ec and velocidad <= min_zona_urbana_ec:
            print("Rango de velocidad permitido")
        else: 
            print("Fuera del límite de velocidad")  
    elif zona == 2:
        if velocidad >= min_zona_rural_ec and velocidad <= min_zona_rural_ec:
            print("Rango de velocidad permitido")
        else: 
            print("Fuera del límite de velocidad")  
    elif zona == 3:
        if velocidad >= min_zona_perimetral_ec and velocidad <= min_zona_perimetral_ec:
            print("Rango de velocidad permitido")
        else: 
            print("Fuera del límite de velocidad")  
    else:
        print("Zona no permitidad")
elif pais == 3:
    if zona == 1:
        if velocidad >= min_zona_urbana_pe and velocidad <= min_zona_urbana_pe:
            print("Rango de velocidad permitido")
        else: 
            print("Fuera del límite de velocidad")  
    elif zona == 2:
        if velocidad >= min_zona_rural_pe and velocidad <= min_zona_rural_pe:
            print("Rango de velocidad permitido")
        else: 
            print("Fuera del límite de velocidad")  
    elif zona == 3:
        if velocidad >= min_zona_perimetral_pe and velocidad <= min_zona_perimetral_pe:
            print("Rango de velocidad permitido")
        else: 
            print("Fuera del límite de velocidad")  
    else:
        print("Zona no permitidad")
else: 
    print("Opción no permitida")