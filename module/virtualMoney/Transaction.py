
class Transaction:
    def __init__(self):
        self.fromId = ""
        self.toId = ""
        self.amount = 0
    def __init__(self, fromId, toId, amount):
        self.fromId = fromId
        self.toId = toId
        self.amount = amount
    def __str__(self):
        return f"{self.fromId} transfers {self.toId} {self.amount} "