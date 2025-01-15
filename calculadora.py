print('*** Calculadora En Python ***')

salir = False
while not salir:
    print(''' -Menu calculadora-
1. Suma 
2. Resta
3. Multiplicacion
4. Division
5. Salir ''')

    opcion = int(input('Eliga una opcion: '))
    if opcion ==1:
        numero_uno = int(input('Ingrese un numero: '))
        numero_dos = int(input('Ingrese otro numero: '))
        print(f'\nSu suma es de {numero_uno + numero_dos}')
    elif opcion ==2:
        numero_uno = int(input('Ingrese un numero: '))
        nummero_dos = int(input('Ingrese otro numero: '))
        print(f'\nSu resta es de {numero_uno - nummero_dos}')
    elif opcion == 3:
        numero_uno = int(input('Ingrese un numero: '))
        nummero_dos = int(input('Ingrese otro numero: '))
        print(f'\nSu multiplicacion es de {numero_uno * nummero_dos}')
    elif opcion == 4:
        numero_uno = int(input('Ingrese un numero: '))
        nummero_dos = int(input('Ingrese otro numero: '))
        print(f'\nSu division es de {numero_uno / nummero_dos}')
    elif opcion == 5:
        salir = True
        print('Saliendo de la calculadora de Murdok! Saludos bro!')
    else:
        print('Ingrese un digito valido! Vuelva a intentarlo.')