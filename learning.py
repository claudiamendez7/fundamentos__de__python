
def saludo(nombre):
    saludo = f"¡Hola, {nombre}!"
    return saludo

nombre = "Alice"
saludo_personalizado = saludo(nombre)

print(saludo_personalizado)

import math

def area_circulo(radio):
    area = math.pi * radio**2
    return area

radio = 5
area_circulo = area_circulo(radio) # type: ignore
print(f"El área del circulo con radio {radio} es: {area_circulo}")

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius 

celsius = 20
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados celsius equivalen a {fahrenheit}grados fahrenheit")

fahrenheit = 100
celsius = fahrenheit_a_celsius(fahrenheit)
print(f"{fahrenheit} grados fahrenheit equivalen a {celsius} grados celsius")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = 5
factorial_n = factorial(numero)
print(F"El factorial de {numero} es: {factorial_n}")

def saludo_procedimiento(nombre):
  print(f"¡Hola, {nombre}!")

nombre = "Alice"
saludo_procedimiento(nombre)
