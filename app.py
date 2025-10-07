## Calculadora
from pickletools import optimize

from errorres import DivisionPorCeroError, EntradaInvalidaError


# funcion suma
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2


def division(num1, num2):
    try:
        if (num2 == 0):
            raise DivisionPorCeroError()
        return num1 / num2
    except ValueError as e:
        print(f"Error {e}")


def menu():
    print(f"Seleccione una opcion:")
    print(f"1-Suma:")
    print(f"2-Resta:")
    print(f"3-Multiplicacion:")
    print(f"4-Division:")
    print(f"5-Salir:")
    option = int(input("Dame una opcion: "))
    return option


def operaciones(option):
    try:
        if option == 5:
            print("Saliendo de la calculadora...")
            return False  # salir del bucle principal

        # 🚫 Validar opción antes de pedir números
        if option not in (1, 2, 3, 4):
            raise EntradaInvalidaError("Opción no válida")

        print("Necesito dos números")
        try:
            number1 = float(input("Dame el primer número: "))
            number2 = float(input("Dame el segundo número: "))
        except ValueError:
            raise EntradaInvalidaError("Debes introducir valores numéricos")

        # Ejecutar la operación seleccionada
        if option == 1:
            print(f"La suma es: {add(number1, number2)}")
        elif option == 2:
            print(f"La resta es: {subtract(number1, number2)}")
        elif option == 3:
            print(f"La multiplicación es: {multiplicacion(number1, number2)}")
        elif option == 4:
            print(f"La división es: {division(number1, number2)}")
        else:
            raise EntradaInvalidaError("Opción no válida")

    except DivisionPorCeroError as e:
        print(f"Error: {e}")
    except EntradaInvalidaError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return True


# Bucle Principal
while True:
    try:
        opcion = menu()
        if not operaciones(opcion):
            break
    except EntradaInvalidaError as e:
        print(f"Error: {e}")
