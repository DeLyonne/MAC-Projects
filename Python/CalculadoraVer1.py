usar_calculadora = True
while usar_calculadora:
    # Solicita al usuario el primer numero y lo convierte a entero.
    numero1_valido = False
    while not numero1_valido:
        try:
            numero1 = float(input("Digite el primer numero: "))
            print("Número válido detectado")
            numero1_valido = True
        except:
            print("Error: Ingrese un numero valido.")

    print("Entrando a nueva operación")
    # Solicita el segundo numero que se usara en la operacion.
    try:
        numero2 = float(input("Digite el segundo numero: "))
    except:
        print("Error: Ingrese un numero valido.")

    # Pide al usuario que elija que operacion matematica quiere realizar.
    operacion = input("Digite la operacion a realizar (+, -, *, /): ")

    # Si el usuario escribe "+", el programa realiza una suma.
    if operacion == "+":
        resultado = numero1 + numero2
        print("Resultado:", resultado)

    # Si el usuario escribe "-", el programa realiza una resta.
    elif operacion == "-":
        resultado = numero1 - numero2
        print("Resultado:", resultado)

    # Si el usuario escribe "*", el programa realiza una multiplicacion.
    elif operacion == "*":
        resultado = numero1 * numero2
        print("Resultado:", resultado)

    # Si el usuario escribe "/", el programa intenta realizar una division.
    elif operacion == "/":

        # Antes de dividir, verifica que el segundo numero no sea cero.
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado:", resultado)

        # Si el segundo numero es cero, muestra un mensaje de error.
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Operacion invalida")
    
    continuar = input("¿Desea realizar otra operacion? (s/n): ")
    if continuar != "s":
        usar_calculadora = False
        print("Gracias por usar la calculadora. ¡Hasta luego!") 
        
