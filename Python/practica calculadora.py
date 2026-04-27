practica = True
while practica:
    # Solicita al usuario el primer numero y lo convierte a decimal.
    try:
        numero1 = float(input("Digite el primer numero: "))
    except:
        print("Error: Ingrese un numero valido.")