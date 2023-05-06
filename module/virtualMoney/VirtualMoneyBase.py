
class VirtualMoneyBase:
    def __init__(self, amount, currency):
        self.currency = currency
        self.amount = amount
    def __repr__(self):
        return f"{self.amount} {self.currency}"
    
    def __str__(self):
        return f"{self.amount} {self.currency}"