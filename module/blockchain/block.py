import hashlib, json

class Block:
    def __init__(self, data):
        self.data = data
        self.prevHash = '-1'
        self.hash = ''
        self.nonce = 0
        self.totalTime = '0'
    
    def hash(block):
        data = str(block.data) + block.prevHash + str(block.nonce)
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def checkHash(block):
        hash = Block.hash(block)
        check = hash.startswith("00")
        return check
