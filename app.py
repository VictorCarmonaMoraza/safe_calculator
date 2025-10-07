##Multiples excepciones
try:
    num = int(input("Dame un numero: "))
    result = 10 / num
except (ZeroDivisionError, ValueError):
    print("Error divsion por cero")
