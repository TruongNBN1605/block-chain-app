from module.blockchain import BlockChain, TransactionBlockchain
from module.virtualMoney import Transaction, HUSTCoin

bc = TransactionBlockchain()

bc.add(Transaction("TruongNBN", "NhatNP", HUSTCoin(1000)))
bc.add(Transaction("TruongNBN", "TuanNM", HUSTCoin(1000)))
bc.add(Transaction("TruongNBN", "VyNT", HUSTCoin(1000)))
bc.add(Transaction("TruongNBN", "SonNT", HUSTCoin(1000)))
bc.add(Transaction("TuanNM", "NhatNP", HUSTCoin(50)))
bc.add(Transaction("TuanNM", "VyNT", HUSTCoin(200)))
bc.add(Transaction("VyNT", "SonNT", HUSTCoin(100)))

print("Tài khoản của TuanNM: ",bc.getBalance("TuanNM"))

print(bc)

print("Kiểm tra BlockChain:", bc.isValid())