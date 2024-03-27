def sumar_n_numeros():
    numeros_a_sumar = int(input('¿Cuántos números quieres sumar: '))
    lista_numeros = []

    for numero in range(0, numeros_a_sumar):
        numero_a_sumar = float(input(f'Ingresa el número {numero + 1} a sumar: '))
        lista_numeros.append(numero_a_sumar)

    return sum(lista_numeros)


def multiplicar_n_numeros():
    numeros_a_multiplicar = int(input('¿Cuántos números quieres multiplicar: '))
    lista_numeros_2 = []

    for numero in range(0, numeros_a_multiplicar):
        numero_a_multiplicar = float(input(f'Ingresa el número {numero + 1} a multiplicar: '))
        lista_numeros_2.append(numero_a_multiplicar)

# Es importante inicializar en 1 porque cuando multiplicas cualquier número por 1, no cambia el valor de ese número.   
    resultado = 1
    for num in lista_numeros_2:
        resultado *= num
    
    return resultado


def dividir_n_numeros():
    dividendo = float(input('Ingresa el dividendo: '))
    divisor = float(input('Ingresa el divisor: '))

# Comprobamos si el divisor es cero para evitar divisiones por cero
    if divisor == 0:
        print("No se puede dividir entre cero, sorry.")
        return None
    
    resultado = dividendo / divisor

    return resultado

# Y = mx + b 
def resolver_para_y():
    pendiente = float(input('Por favor ingresa la pendiente: '))
    ordenada_origen = float(input('Por favor ingrese la ordenada al origen: '))
    punto_x = int(input('Ingrese un punto en x: '))
    resultado = (pendiente * punto_x) + ordenada_origen

    return {'resultado':resultado, 'pendiente':pendiente, 'ordenada_origen': ordenada_origen, 'punto_x': punto_x}


