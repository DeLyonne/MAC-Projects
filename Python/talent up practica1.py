y=input('Ingrese un número entero entre 0 y 1024 -- ')

x=int(y)

a=0

b=1024

test=True

if x == 0:

    print('Su número es 0, gracias por jugar.')

    test=False

else:

    if x == 1024:

        print('Su número es 1024, gracias por jugar.')

        test=False

    while test == True:

        n=int((a+b)/2)

        if n == x:

            print('Su número es ', n, ', gracias por jugar.')

            break

        else:

            if n < x:

                a=n

            else:

                b=n