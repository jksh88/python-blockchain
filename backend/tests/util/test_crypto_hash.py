from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
  # Should create the same hash with arguments of different data types no matter the order
  assert crypto_hash([1], 2, 'three') == crypto_hash('three', 2, [1])
  assert crypto_hash('Joe') == 'ba519d38f163da3f0fc9f98d2fa78e4dbc497e789145d40166c2d74a2caf4bd8'
