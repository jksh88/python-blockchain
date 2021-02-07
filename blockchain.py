
class Block:
  '''
  block: a unit of storage
  '''
  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return f'Block - data: {self.data} '




class Blockchain:
  '''
  a public ledger of transactions.
  implemented as a list of blocks - datasets of transactions
  '''
  def __init__(self):
    self.chain = []

  def add_block(self, data):
    self.chain.append(Block(data))

  def __repr__(self):
    return f'Blockchain: {self.chain}'

blockchain = Blockchain()
blockchain.add_block('one')
blockchain.add_block('two')

print(blockchain)