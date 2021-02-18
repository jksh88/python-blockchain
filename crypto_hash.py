import hashlib
import json


def crypto_hash(*args):
  '''
  Return a sha-256 hash of the given arguments
  '''
  stringified_args = sorted(map(lambda data: json.dumps(data) , args))
  joined_data = ''.join(stringified_args)
  # print(f'stringified_args: {args}')
  # print(f'joined_data: {joined_data}')
  return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
  print(f"cryto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
  print(f"crypto_hash([3], 2,'one'): {crypto_hash([3], 2, 'one')}")

if __name__ == '__main__':
  main()