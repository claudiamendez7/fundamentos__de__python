# Solicita al usuario que inserte una moneda en la máquina expendedora de Coke, una por vez, informándole al usuario el monto adeudado cada vez

precio = 50
denominaciones = [25, 10, 5]
ingresado = 0
adeudado = precio

while adeudado > 0:
    moneda = int(input("Ingresa una moneda (25, 10, o 5 centavos): "))
    if moneda in denominaciones :
        ingresado += moneda
        adeudado -= moneda
        print("Monto adeudado: {} centavos".format(adeudado))
    else:
        print("Moneda no aceptada. Ingresa una moneda de 25, 10 o 5 centavos")
            
if ingresado > precio:
    cambio = ingresado - precio
    print("Cambio: {} centavos".format(cambio)) 