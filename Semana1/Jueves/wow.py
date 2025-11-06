chocolate = 4000
vainilla = 3500
topping = 1000


helado = input("Ingrese el sabor: ").lower()

if helado == "chocolate":
    precio = chocolate
elif helado == "vainilla":
    precio = vainilla

else:
    print("no existe, bobo bobo bobo")
    precio = None


if precio is not None:
    opcion = input("Quiere topping? si/no: ").lower()
    if opcion == "si":
        precio +=topping
        print(precio)
    else:
        print(precio)