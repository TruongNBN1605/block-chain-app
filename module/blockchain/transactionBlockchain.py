from module.virtualMoney import Transaction, VirtualMoneyBase
from .blockchain import BlockChain

class TransactionBlockchain(BlockChain):
    def __init__(self):
        super().__init__()
    
    def add(self, data):
        if isinstance(data, Transaction):
            super().add(data)

    def getBalance(self, userId):
        rs = VirtualMoneyBase(0, self.chain[-1].data.amount.currency)
        for block in self.chain:
            if isinstance(block.data, Transaction):
                if block.data.fromId == userId:
                    rs -= block.data.amount
                if block.data.toId == userId:
                    rs += block.data.amount
        return rs