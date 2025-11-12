inventario = []
opcion = 0

def AgresarProducto():
      Nombre = input("Ingrese el nombre del producto: ")
      precio = input("ingrese el precio del producto: ")
      cantidad = input("Ingrese la cantidades de productos que desea: ")

      productos = {f"Nombre: ", Nombre, " Precio: ", precio, " Cantidad: ", cantidad}
      inventario.append()

      while not Nombre.isalpha() and precio.isdigit() and precio.replace('.', '', 1).isdigit():
            print("Error, No se han podido gruardar la informacion correctamente verifique que los datos que esta ingresando sean correctos: ")
            Nombre = input("Ingrese el nombre del producto: ")
            precio = input("ingrese el precio del producto: ")
            cantidad = input("Ingrese la cantidades de productos que desea: ")
def MostrarInventario():
      if not inventario:
            print("No se a encontrado ningun dato: ")
      else 
















print("Menu: \n"
               "---------\n" \
               "1 Agregar producto: \n"
               "2 Mostrar inventario: \n" \
               "3 Calcular estadísticas: \n"
               "4 Salir")

opcion = input("Escoge un numero dependiedo de la accion que quiera realizar: ")

while not opcion.isdigit():
    print("Opcion no valida, por favor vuelva a intentarlo: ")
    opcion = input("Escoge un numero dependiedo de la accion que quiera realizar: ")

opcion = int(opcion)

if opcion <= 0 and opcion >=5:
        print = ("Opcion no valida vuelva intentarlo")
        opcion = input("Escoge un numero dependiedo de la accion que quiera realizar: ")

print("no paso nada")