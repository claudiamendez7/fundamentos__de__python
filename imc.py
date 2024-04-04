# Calcule el IMC de una persona basada en su peso en kilogramos y estatura en metros

peso = float(input("Introduzca su peso en kg: "))
altura = float(input("Introduzca su altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    resultado = "Bajo peso"
elif imc < 25:
    resultado = "Normal"
else:
    resultado = "Sobrepeso"
    
print(f"Su IMC es: {imc}. Su estado es: {resultado}. ")  
    