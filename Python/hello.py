# preguntar por nombre
name = input ("Whats' your name? ")

# Remover cualquier barra o espacio blanco del str o string
# Si quiero remover algun caracter o letras o numeros de la variable, puedo agregarlos como por ejemplo .strip("Y aqui dentro iria lo que quiero evitar que se escriba")
name = name.strip()

# Sirve para colocarle mayuscula a la variable que se usara sin importar como se haya escrito. Esto solo lo aplica al primer str, no a los demas como apellidos
name = name.capitalize()

# Si quiero darle mayuscula a cualquier str escrito y no solo al primero
name = name.title()

# Para simplificar la cantidad de lineas que existen, tambien se pueden encadenar las funciones de una variable como por ejemplo abajo:
# name = input ("Whats' your name? ").strip().title()    Esto arrojara el mismo resultado a que si lo separara en diferentes lineas. A preferencia
# Este tipo de funciones que van dentro de variables se les llama "methods" o metodos.

# Split. Sirve para dividir nombres y apellidos. Aqui se crea una nueva variable que es llamada first y la otra last.
# Lo que significa que son una sola, dividida por coma y que sacan la informacion de otra variable que es "name"
# Entonces, uno escribe nombre y apellido que pasa a ser parte de "name" y luego name pasa a ser parte de first y last
first, last = name.split(" ")

#saludar al usuario
print ("hello,", name)
print ("hello, " + name)
print ("hello," , end=" ")
print (name, end=". ")
print (f"hello, {name}")

# ejemplo de cambios enviados a github
print("Hola hector, este es un cambio enviado a github")