
def main():

    menu= {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    order_total = 0.0
    while True:
        try:
            item = input("Ingrese un artículo de su pedido: ")
        except EOFError:
            break
        item = item.upper()
        if item in menu:
                order_total += menu[item]
        elif item == "CONTROL-D":
            print(f"El total de su pedido es ${order_total:.2f}")
            break
        else: 
            print("Artículo inválido")
    if __name__ == "__main__":
        main()