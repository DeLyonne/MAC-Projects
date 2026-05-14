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
    numero1 = pedir_numero("Ingrese el primer numero: ")
    numero2 = pedir_numero("Ingrese el segundo numero: ")

    # Pide al usuario que elija que operacion matematica quiere realizar.
    operacion_valida = False
    while not operacion_valida:
        operacion = input("Digite la operacion a realizar (+, -, *, /): ")

            # Si el usuario escribe "+", el programa realiza una suma.
        if operacion == "+":
            resultado = numero1 + numero2
            print("Resultado:", numero1, operacion, numero2, "=", resultado)
            operacion_valida = True

            # Si el usuario escribe "-", el programa realiza una resta.
        elif operacion == "-":
            resultado = numero1 - numero2
            print("Resultado:", numero1, operacion, numero2, "=", resultado)
            operacion_valida = True

            # Si el usuario escribe "*", el programa realiza una multiplicacion.
        elif operacion == "*":
            resultado = numero1 * numero2
            print("Resultado:", numero1, operacion, numero2, "=", resultado)
            operacion_valida = True

        # Si el usuario escribe "/", el programa intenta realizar una division.
        elif operacion == "/":

            # Antes de dividir, verifica que el segundo numero no sea cero.
            if numero2 != 0:
                resultado = numero1 / numero2
                print("Resultado:", numero1, operacion, numero2, "=", resultado)
                operacion_valida = True
                
            # Si el segundo numero es cero, muestra un mensaje de error.
            else:
                print("Error: No se puede dividir por cero.")
        else:
            print("Operacion invalida")
    
    # Tenia la variable de continuar aqui pero la movi para que el programa sea mas fluida y no se repita el codigo de pedir numeros y operacion si el usuario quiere hacer otra operacion.
    while True:
        continuar = input("¿Desea realizar otra operacion? (s/n): ").lower().strip()
        if continuar in ("s", "si"):
            break
        elif continuar in ("n", "no"):
            usar_calculadora = False
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break
        else:
            continuar = input("Respuesta invalida. Por favor, ingrese 's' para sí o 'n' para no: ").lower().strip()


# Mejoras por hacer: Sacar el print de los if, tambien arreglar los inputs para las operaciones a elegir como con continuar, no repetirt el mismo print en cada if, crear una funcion para cada operacion matematica, agregar mas operaciones como potencia, raiz cuadrada, etc.
# Buen trabajo, sigue asi!