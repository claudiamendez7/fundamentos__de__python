def es_palindromo(texto):
    """Determina si una palabra es un palíndromo."""
    texto_sin_mayusculas = texto.lower()
    texto_sin_espacios = "" .join(c for c in texto_sin_mayusculas if c.isalnum())
    texto_invertido = texto_sin_espacios[::-1]
    return texto_sin_espacios == texto_invertido

palabra = "Anita lava la tina"

if es_palindromo(palabra):
    print(f"la palabra '{palabra}' es un palíndromo")
else:
    print(f"La palabra '{palabra}' no es un palíndromo")