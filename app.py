try:
    num = int(input("Enter a number: "))
    resultado = 10 / num
    print(resultado)
except ZeroDivisionError:
    print("Error: No se permiten las divisiones por cero")
except ValueError:
    print("Error: Invalid input. Please enter a valid number")
