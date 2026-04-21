usar_calculadora = True
while usar_calculadora:
    # Solicita al usuario el primer numero y lo convierte a entero.
    numero1 = int(input("Digite el primer numero: "))

    # Solicita el segundo numero que se usara en la operacion.
    numero2 = int(input("Digite el segundo numero: "))

    # Pide al usuario que elija que operacion matematica quiere realizar.
    operacion = input("Digite la operacion a realizar (+, -, *, /): ")

    # Si el usuario escribe "+", el programa realiza una suma.
    if operacion == "+":
        resultado = numero1 + numero2
        print("El resultado de la suma es:", resultado)

    # Si el usuario escribe "-", el programa realiza una resta.
    elif operacion == "-":
        resultado = numero1 - numero2
        print("El resultado de la resta es:", resultado)

    # Si el usuario escribe "*", el programa realiza una multiplicacion.
    elif operacion == "*":
        resultado = numero1 * numero2
        print("El resultado de la multiplicacion es:", resultado)

    # Si el usuario escribe "/", el programa intenta realizar una division.
    elif operacion == "/":

        # Antes de dividir, verifica que el segundo numero no sea cero.
        if numero2 != 0:
            resultado = numero1 / numero2
            print("El resultado de la division es:", resultado)

        # Si el segundo numero es cero, muestra un mensaje de error.
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Operacion invalida")
    
    continuar = input("¿Desea realizar otra operacion? (s/n): ")
    if continuar != "s":
        usar_calculadora = False
        print("Gracias por usar la calculadora. ¡Hasta luego!") 
        
