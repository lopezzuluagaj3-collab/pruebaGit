"""
num = int(input(" ingresa un numero: "))


for i in range(num):
        i +=1
        if i % 2 == 0:
            print(f"El numero ingresado {i} es par")
        else:
            print(f"El numero ingresado {i} es Impar")
"""

#while

"""numero = int(input(" ingresa un numero: "))

while numero > 0:
    print(numero)
    numero -= 1"""

#primer ejercicio panaderia

"""panes = int(input(" ingresa la cantidad de panes que deseas comprar: "))

pan = 300

if panes <= 0:
    print(" cantidad no valida")

elif panes >= 50:
    total = panes * pan
    descuento = total * 0.2
    print(f" El total a pagar por {panes} panes es de: ", total - descuento)

elif panes >= 20:
    total = panes * pan
    descuento = total * 0.1
    print(f" El total a pagar por {panes} panes es de: ", total - descuento)"""


#Gimnasio Solo Leveling Fit


"""dias = int(input(" ingresa la cantidad de dias a asistido al gym: "))

if dias < 0 or dias >= 8:
    print(" cantidad no valida")

elif dias == 1 or dias == 0: 
    print ("has asistido " + str(dias) + " días No aflojes, tú puedes mejorar más")

elif dias == 2 or dias == 3:
    print ("¡Sigue así! has asistido " + str(dias) + " días Bien, pero puedes dar más")

elif dias >= 4:
    print ("¡Excelente disciplina! has asistido " + str(dias) + " días y ganas 1 punto de energía")"""

#  5. Librería “El Saber” — Descuento estudiante + cupón

"""print(" Bienvenido a la librería, si eres estudiante tienes un 15% de descuento en tu compra \n Además, si tienes un cupón de descuento del 10% no puedes aplicarlo sobre sobre el \n decuento de estudiante ")
usuario =int(input(" Si tienes un cupón de descuento escribe 1, si eres un estudianteescribe 2 \n:"))
libros = int(input(" ingresa la cantidad de libros que deseas comprar: "))

precio = 25000

if usuario <= 0:    
    print(" opción no valida ")


elif usuario == 1:
    total = libros * precio
    descuento = total * 0.1
    print(f" El total a pagar por {libros} libros es de: ", total - descuento)

elif usuario == 2:
    total = libros * precio
    descuento = total * 0.15
    print(f" El total a pagar por {libros} libros es de: ", total - descuento)
else:
    print(" opción no valida ")"""


#Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA

"""print(" Bienvenido al restaurante 'El Sabor Colombiano' \n Nuestro menú del día cuesta $12.000 y la bebida cuesta $3.000):")
menus = int(input(" ingresa la cantidad de menús que deseas pedir: "))
Platos = input(" deseas pedir la bebida? (si/no): ")
plato = 12000
bebida = 3000

comida = plato * menus

if menus <= 0:
    print(" cantidad no valida ")

elif Platos == "si":
    total = comida + bebida
    iva = total * 0.08
    print(f" El total a pagar por el plato y la bebida es de: ", total + iva)

elif Platos == "no":
    total = comida
    iva = total * 0.08
    print(f" El total a pagar por el plato es de: ", total + iva)

else:
    print(" opción no valida ")"""


#9. Supermercado “AhorroMax” — Descuentos y envío

numero = int(input("ingresa todos los productos que deseas comprar: "))

productos = 2000
total = productos * numero

if numero <= 0:
    print(" cantidad no valida ")
elif numero >= 30:
    descuento = total * 0.15
    final = total - descuento
    if final >= 50000:
        print(f" El total a pagar por {numero} productos es de: ", final + 5000)
    else:
        print(f" El total a pagar por {numero} productos es de: ", final)
elif numero >= 10:
    descuento = total * 0.05
    final = total - descuento
    if final >= 50000:
        print(f" El total a pagar por {numero} productos es de: ", final + 5000)
    else:
        print(f" El total a pagar por {numero} productos es de: ", final)