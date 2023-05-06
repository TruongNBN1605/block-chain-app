
from datetime import datetime, timedelta
from .block import Block

class BlockChain:
    def __init__(self):
        self.chain = []
        firstBlock = Block('First Block')
        firstBlock.hash = Block.hash(firstBlock)
        self.chain.append(firstBlock)
    
    def add(self, data):
        lastBlock = self.chain[-1]
        newBlock = Block(data)
        newBlock.prevHash = lastBlock.hash
        newBlock.nonce = lastBlock.nonce
        start = datetime.now()
        while Block.checkHash(newBlock) == False:
            newBlock.nonce = newBlock.nonce + 1
            newBlock.hash = Block.hash(newBlock)
        end = datetime.now()
        newBlock.totalTime = str(end - start)
        self.chain.append(newBlock)

    def isValid(self):
        for i in range(1, len(self.chain)):
            curBlock = self.chain[i]
            prevBlock = self.chain[i-1]
            if Block.checkHash(curBlock) == False:
                return False
            if Block.hash(curBlock) != curBlock.hash:
                return False
            if (Block.hash(prevBlock) != curBlock.prevHash):
                return False
        return True

    # DEV: print blockchain data
    def print(self):
        for block in self.chain:
            print("Data:", block.data)
            print("PrevHash:", block.prevHash)
            print("Hash:", block.hash)
            print("Nonce:", block.nonce)
            print("totalTime:", block.totalTime)
            print()
