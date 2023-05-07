
class VirtualMoneyBase:
    def __init__(self, amount = 0, currency = None):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    def __add__(self, other):
        if self.currency == other.currency:
            return VirtualMoneyBase(self.amount + other.amount, self.currency)
        else:
            raise ValueError("Cannot add different currencies")
        
    def __sub__(self, other):
        if self.currency == other.currency:
            return VirtualMoneyBase(self.amount - other.amount, self.currency)
        else:
            raise ValueError("Cannot add different currencies")
            
    def __iadd__(self, other):
        if self.currency == other.currency:
            self.amount += other.amount
        else:
            raise ValueError("Cannot add different currencies")
        return self
    
    def __isub__(self, other):
        if self.currency == other.currency:
            self.amount -= other.amount
        else:
            raise ValueError("Cannot add different currencies")
        return self