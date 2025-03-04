class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount + other.amount,
                self.currency
            )
        raise RuntimeError("Mismatched currencies!")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(
                self.amount - other.amount,
                self.currency
            )
        raise RuntimeError("Mismatched currencies!")

    def __mul__(self, number):
        return Money(
            self.amount*number,
            self.currency
        )

a = Money(10, "EUR") + Money(20, "EUR")
print(a.amount, a.currency)
b = Money(20, "EUR") * 5
print(b.amount, b.currency)
