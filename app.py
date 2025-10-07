##Excepciones personalizadas

def withdraw(amount):
    if amount < 0:
        raise ValueError("No puedes retirar menos de cero")
    print(f"Tu has retirado ${amount}")


try:
    withdraw(-50)
except ValueError as e:
    print(f"Error: {e}")
