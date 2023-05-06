from module.blockchain import BlockChain, Block

bc = BlockChain()
bc.add("Đại học Bách Khoa Hà Nội")
bc.add("Mật mã và Độ Phức tạp thuật toán")
bc.add("Nhóm 9")

# bc.chain[1].data = "RHUST"
# bc.chain[1].hash = Block.hash(bc.chain[1])
# bc.chain[2].prevHash = bc.chain[1].hash
# bc.chain[2].hash = Block.hash(bc.chain[2])
# bc.chain[3].prevHash = bc.chain[2].hash
# bc.chain[3].hash = Block.hash(bc.chain[3])

bc.print()

print("Kiểm tra BlockChain:", bc.isValid())