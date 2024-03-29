from funciones_calculadora import *

#Importamos librerías para poder graficar
import numpy as np
import matplotlib.pyplot as plt

while True:
    print('''
          Bienvenido a mi calculadora, por favor ingresa la opción que desees.
-------------------------------------------------------------------------------
          
          1) Hacer una sumar de N números.
          2) Hacer una multiplicación.
          3) Hacer una división de 2 números.
          4) Resolver la posición en Y (ecuación y = mx + b)
          
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

    # y = mx + b
    elif opcion == 4:
             
        resultado = resolver_para_y()
        print(f'El resultado es: {resultado}')

        x = np.linspace(-10,10)
        y = resultado['pendiente'] * x + resultado['ordenada_origen']

        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth=2.0)
        ax.plot(resultado['punto_x'], resultado['resultado'], 'yo')

        ax.grid(True, linestyle='-')
        

        plt.show()

print('------------------------------------------------------')
print('Bye Bye, gracias por usar mi calculadora')