import informacion

cantidad_pacientes = int(input("¿Cuántos pacientes desea ingresar?: "))
for i in range(cantidad_pacientes):
    paciente = input("Ingrese nombre apellido y fecha de nacimiento: ")
    datos = paciente.split()

    nombre = " ".join(datos[:-1])
    año_nacimiento = int(datos[-1]) 
    informacion.agregar_nombre(nombre)
    informacion.agregar_edad(año_nacimiento)


informacion.imprimir_nombres()
informacion.imprimir_edades()
informacion.paciente_mayor()

