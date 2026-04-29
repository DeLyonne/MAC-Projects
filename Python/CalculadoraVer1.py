# Crear funcion
def pedir_numero(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except:
            print("Error: Ingrese un numero valido.")
        

usar_calculadora = True
while usar_calculadora:
    numero_valido1 = pedir_numero("Ingrese el primer numero: ")
    numero_valido2 = pedir_numero("Ingrese el segundo numero: ")

    # Pide al usuario que elija que operacion matematica quiere realizar.
    operacion_valida = False
    while not operacion_valida:
        operacion = input("Digite la operacion a realizar (+, -, *, /): ")

            # Si el usuario escribe "+", el programa realiza una suma.
        if operacion == "+":
            resultado = numero_valido1 + numero_valido2
            print("Resultado:", resultado)
            operacion_valida = True

            # Si el usuario escribe "-", el programa realiza una resta.
        elif operacion == "-":
            resultado = numero_valido1 - numero_valido2
            print("Resultado:", resultado)
            operacion_valida = True

            # Si el usuario escribe "*", el programa realiza una multiplicacion.
        elif operacion == "*":
            resultado = numero_valido1 * numero_valido2
            print("Resultado:", resultado)
            operacion_valida = True  

        # Si el usuario escribe "/", el programa intenta realizar una division.
        elif operacion == "/":

            # Antes de dividir, verifica que el segundo numero no sea cero.
            if numero_valido2 != 0:
                resultado = numero_valido1 / numero_valido2
                print("Resultado:", resultado)
                operacion_valida = True
                
            # Si el segundo numero es cero, muestra un mensaje de error.
            else:
                print("Error: No se puede dividir por cero.")
        else:
            print("Operacion invalida")
    
    
    continuar = input(str("¿Desea realizar otra operacion? (s/n): "))
    if continuar != "s":
        usar_calculadora = False
        print("Gracias por usar la calculadora. ¡Hasta luego!") 
        
