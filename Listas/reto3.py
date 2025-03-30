print("Segunda es Todo")
print("1. Añadir plato al menú")
print("2. Buscar en el menú")
print("3. Eliminar plato del menú")
print("4. Mostrar platos del menú")

opcion = int(input("Elija una opción: "))

menu = ["Encebollado", "Fritada", "Pollo a la plancha"]

if opcion == 1:
    plato = input("Ingrese el plato: ")
    menu.append(plato)
    print(F"Menú actualizado {menu} ")
elif opcion == 2:
    plato = input("Ingrese el plato a buscar: ")
    if (plato in menu):
        print(F"Plato {plato} encontrado")
    else: 
        print(F"Plato no encontrado")
elif opcion == 3: 
    print(menu)
    plato = input("Ingrese el plato a eliminar: ")
    menu.remove(plato)
    print(F"Menú actualizado {menu}")
elif opcion == 4:
    print(F"Menú {menu}")
else:
    print("Opción no válida")


