num1 = int(input('Introduzca un numero entero: '))
num2 = int(input('Introduzca un numero entero: '))
num3 = int(input('Introduzca un numero entero: '))
if num1 > num2 and num1 > num3:
    print(f'El número mayor es {num1}')
else:
    if num2 > num3:
        print(f'El número mayor es {num2}')
    else:
        print(f'El número mayor es {num3}')
