def datos(nombre, apellido, edad, mensaje="Hola"):
    edad = int(edad)
    if edad < 18:
        print(F"{mensaje} {nombre} {apellido} es menor de edad")
    else:
        print(F"{mensaje} {nombre} {apellido} es mayor de edad")