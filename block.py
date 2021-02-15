import time

class Block:
  '''
  block: a unit of storage
  '''
  def __init__(self, timestamp, last_hash, hash, data):
    self.timestamp = timestamp
    self.last_hash = last_hash
    self.hash = hash
    self.data = data

  def __repr__(self):
    return (
      'Block('
      f'timestamp: {self.timestamp}, '
      f'last_hash: {self.last_hash}, '
      f'hash: {self.hash}, '
      f'data: {self.data})'
    )

  @staticmethod
  def mine_block(last_block, data):
    '''
    mines a block based on the given last_block and data
    '''
    timestamp = time.time_ns()
    last_hash = last_block.hash
    hash = f'{timestamp}-{last_hash}'

    return Block(timestamp, last_hash, hash, data)

  @staticmethod
  def genesis():
    '''
    Generates the genesis block
    '''
    return Block(1, 'genesis_last_hash', 'genesis_hash', [])

def main():
  genesis_block = Block.genesis()
  block = Block.mine_block(genesis_block, 'foo')
  print(block)

if __name__ == '__main__':
  main()

