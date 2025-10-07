class WithdrawError(Exception):
    def __init__(self, amount, message="Cantidad no válida para retiro"):
        self.amount = amount
        self.message = message
        super().__init__(f"{message}: {amount}")
