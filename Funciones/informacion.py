nombre_paciente = []
edad = []
def agregar_nombre(nombre_completo):
    nombre_paciente.append(nombre_completo)

def agregar_edad(año_nacimiento):
    edad_actual = 2025 - año_nacimiento
    edad.append(edad_actual)

def imprimir_nombres():
    print(F"Pacientes {nombre_paciente} ")

def imprimir_edades():
    print(F"Edades {edad} ")

def paciente_mayor():
    max_edad = max(edad)  
    index = edad.index(max_edad) 
    nombre_mayor = nombre_paciente[index]
    print(F"{nombre_mayor} con la edad de {max_edad} es mayor a los demás pacientes")

    