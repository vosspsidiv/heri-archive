# HERI Signal Extractor
from PIL import Image
import struct, sys

if len(sys.argv) != 2:
    print("Usage: python3 extract_key.py <image.png>")
    sys.exit(1)

img = Image.open(sys.argv[1]).convert("RGB")
width, height = img.size

raw_bits = []
for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        raw_bits.append(r & 1)

length_val = 0
for b in raw_bits[:32]:
    length_val = (length_val << 1) | b

if length_val == 0 or length_val > 512:
    print("No hidden data found.")
    sys.exit(1)

msg = ''
for i in range(0, length_val * 8, 8):
    byte_val = 0
    for b in raw_bits[32 + i:32 + i + 8]:
        byte_val = (byte_val << 1) | b
    msg += chr(byte_val)

print(f"Recovered: {msg}")

