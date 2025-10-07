from ErrorPersonalizado import WithdrawError


def withdraw(amount):
    if amount < 0:
        raise WithdrawError(amount)
    print(f"Has retirado ${amount}")


try:
    withdraw(-50)
except WithdrawError as e:
    print(f"Error: {e.message} (monto: {e.amount})")
