"""door = True

if door:
    print("La puerta está abierta")
else:
    print("La puerta está cerrada")"""

#ejercicio edad

edad = int(input("Ingrese su edad: "))
if edad <= 0:
    print("Edad inválida")

elif edad >= 110:
    print("Edad inválida")

elif edad >= 18:
    print("Eres mayor de edad")

else:
    print("Eres menor de edad")