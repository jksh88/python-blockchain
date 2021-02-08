class Block:
  '''
  block: a unit of storage
  '''
  def __init__(self, data):
    self.data = data

  def __repr__(self):
    return f'Block - data: {self.data}'

def main():
  block = Block('foo')
  print(block)

  print(f'block.py__name__:{__name__}')

if __name__ == '__main__':
  main()

