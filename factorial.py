def factorial(n):
    """Calcula el factorial de un numero."""
    resultado = 1
    for i in range(1, n + 1):
       resultado *= i
    return resultado

numero = 5
factorial_de_numero = factorial(numero)

print(f"El factorial de {numero} es {factorial_de_numero}")
