practica = False
while not practica:
    # Solicita al usuario el primer numero y lo convierte a decimal.
    try:
        numero1 = float(input("Digite el primer numero: "))
        practica = True
    except:
        print("Error: Ingrese un numero valido.")

print("Gracias por usar la calculadora. ¡Hasta luego!").lower()