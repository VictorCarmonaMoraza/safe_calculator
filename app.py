## Calculadora
from pickletools import optimize


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
            raise ValueError("No se puede dividir entre cero")
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
            return False  # ← salimos del bucle principal
        else:
            print("Necesito dos números")
            number1 = float(input("Dame el primer número: "))
            number2 = float(input("Dame el segundo número: "))

            if option == 1:
                print(f"La suma es: {add(number1, number2)}")
            elif option == 2:
                print(f"La resta es: {subtract(number1, number2)}")
            elif option == 3:
                print(f"La multiplicación es: {multiplicacion(number1, number2)}")
            elif option == 4:
                print(f"La división es: {division(number1, number2)}")
            else:
                print("La opción no es válida")
        return True  # continuar el programa
    except ValueError as e:
        print(f"Error: entrada no válida {e}")
    except ZeroDivisionError as e:
        print("Error: no se puede dividir por cero {e}")
    return True


# Bucle Principal
while True:
    opcion = menu()
    if not operaciones(opcion):
        break
