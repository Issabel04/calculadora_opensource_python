from funciones_calculadora import *

while True:
    print('''
          Bienvenido a mi calculadora, por favor ingresa la opción que desees.
-------------------------------------------------------------------------------
          
          1) Hacer una sumar de N números.
          2) Hacer una multiplicación.
          3) Hacer una división de 2 números.
          
          0) Salir del programa.
          ''')
    
    opcion = int(input('> '))

    if opcion == 0 :
        break

    elif opcion == 1:
        resultado = sumar_n_numeros()
        print(f'El resultado de tu suma es {resultado}')

    elif opcion == 2:
        resultado = multiplicar_n_numeros()
        print(f'El resultado de tu multiplicación es {resultado}')

    elif opcion == 3:
        resultado = dividir_n_numeros()
        print(f'El resultado de tu divisón es {resultado}')