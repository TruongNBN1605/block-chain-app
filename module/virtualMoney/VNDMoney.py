from .VirtualMoneyBase import VirtualMoneyBase

class VND(VirtualMoneyBase):
    def __init__(self, amount):
        super().__init__(amount, "VND")
