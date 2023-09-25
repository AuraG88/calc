import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def main():
    # Solicitamos los números a sumar, restar, multiplicar o dividir
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    # Elegimos la operación a realizar
    operacion = input("¿Qué operación quieres realizar? (sumar, restar, multiplicar o dividir): ")

    # Realizamos la operación
    if operacion == "sumar":
        resultado = sumar(a, b)
    elif operacion == "restar":
        resultado = restar(a, b)
    elif operacion == "multiplicar":
        resultado = multiplicar(a, b)
    else:
        resultado = dividir(a, b)

    # Mostramos el resultado
    print("El resultado es:", resultado)

if __name__ == "__main__":
    main()
