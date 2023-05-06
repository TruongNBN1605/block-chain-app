from .VirtualMoneyBase import VirtualMoneyBase

class HUSTCoin(VirtualMoneyBase):
    def __init__(self, amount):
        super().__init__(amount, "HustCoin")
