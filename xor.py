# HERI data recovery utility
# Decrypts archived signal data using XOR cipher
# Usage: python3 xor.py <hex_encoded_data> <key>

import sys

if len(sys.argv) != 3:
    print("Usage: python3 xor.py <hex_data> <key>")
    sys.exit(1)

hex_data = sys.argv[1]
key      = sys.argv[2]

try:
    data = bytes.fromhex(hex_data)
except ValueError:
    print("Error: invalid hex data")
    sys.exit(1)

result = ''
for i, b in enumerate(data):
    result += chr(b ^ ord(key[i % len(key)]))

print(result)
