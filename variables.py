print("*"*20)
print("ejercicio 1: sumar dos numeros")
print("*"*20)

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

print(f"resultado {numero1 + numero2}")


print("*"*20)
print("ejercicio 2: area de un rectangulo")
print("*"*20)

base =float(input("ingrese la base del rectangulo:"))
altura = float(input("ingrese la altura del rectangulo:"))

print(f"el area del rectangulo es: {base * altura}")


print("*"*20)
print("ejercicio 3: minutos a horas")
print("*"*20)

minutos_totales = int(input("ingrese la cantidad de minutos: "))
horas = minutos_totales // 60
minutos = minutos_totales % 60

print(f"{minutos_totales} minutos son {horas} horas y {minutos} minutos.")


print("*"*20)
print("ejercicio 4: precio con descuento")
print("*"*20)

precio    = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento / 100)
precio_final = precio - valor_descuento

print(f"El precio final con descuento es: {precio_final}")



print("*"*20)
print("ejercicio 5: intercambio de variables")
print("*"*20)

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

auxiliar = a
a = b
b = auxiliar

print(f"Después del intercambio, a = {a} , b = {b}")



print("Taller: Punto 1")

base = float(input("Ingrese el ancho del terreno en metros: "))
altura = float(input("Ingrese el largo del terreno en metros: "))

print(f"El perímetro del rectángulo es: {(base*2) + (altura*2)}")


print("Taller: Punto 2")



numero1 = float(input("Ingrese el número 1: "))
numero2 = float(input("Ingrese el número 2: "))
numero3 = float(input("Ingrese el número 3: "))

print(f"El promedio de los números es {(numero1 + numero2 + numero3) / 3}")




pesos = float(input("Ingrese los pesos para convertir a dólar porfa"))

dolar = pesos / 4000

print("Este es el valor en dólares, amo:", dolar)



