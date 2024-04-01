# Cuando se envían mensajes de texto o se tuitea, no es raro abreviar las palabras para ahorrar tiempo o espacio, como por ejemplo omitiendo las vocales, tal y como Twitter fue originalmente llamado "twttr". En un archivo llamado twttr.py, implementa un programa que solicite al usuario una cadena de texto y luego muestre esa misma cadena, pero sin todas las vocales (A, E, I, O y U), ya sea que hayan sido ingresadas en mayúscula o minúscula.

def main():
    palabra = input("Ingrese un texto: ")
    resultado = twttrr(palabra)
    print("La palabra abreviada es: " + ''.join(resultado))

def twttrr(pal):
   pal = pal.lower()
   sal = []
   for z in range(len(pal)):
       if pal[z] not in ["a", "e", "i", "o", "u", " "]:
           sal.append(pal[z])
   return sal
     
if __name__ == "__main__":
   main() 