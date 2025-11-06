#solicita el nombre del producto
nombre = input("Ingresa el nombre del producto: ")

#While not se utiliza para que se siga pidiendo el nombre hasta que se ingrese un valor válido (solo letras)
#While not significa "mientras no", mientras no se compla la condición, se ejecuta el bloque de código dentro del while
# .isalpha() comprueba que el nombre solo contenga letras
while not nombre.isalpha():
    #Este mensage se muestra cuando el dato ingresado no sea in string
    print("Error: el nombre solo puede tener letras: ")
    #Se vuelve a solicitar el nombre del producto
    nombre = input("Ingresa el nombre del producto: ")

#Solicita la cantidad de productos que se desean comprar
cantidad = input("Escribe la cantidad de productos: ")

# .isdigit() comprueba que el dato ingresado sea un integer positivo
while not cantidad.isdigit():
    print("Error: la cantidad debe ser un número entero: ")
    cantidad = input("Escribe la cantidad de productos: ")

#Solicita el precio del producto
precio = input("Ingresa el precio del productos: ")

# .replace('.', '', 1) permite que el número tenga un solo punto decimal
# .isdigit() comprueba que el dato ingresado sea un número (entero o decimal
while not precio.replace('.', '', 1).isdigit():
    print("Error: el precio debe ser un número válido: ")
    precio = input("Ingresa el precio del productos\n: ")
#se convierte el precio a float y la cantidad a integer para realizar el cálculo del costo total
precio = float(precio)
costo_total = precio * int(cantidad)


#Imprime el resumen de la compra
print(f"El producto comprado fue {nombre}. \nLas cantidades pedidas fueron {cantidad}. \nEl precio del producto es {precio}. \nEl costo total es {costo_total}.")
