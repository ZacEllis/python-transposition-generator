#!/usr/bin/env python3

from random import shuffle

PLAINTEXT = "" # Change this

BLOCK_SIZE = 1 # Change this
BLOCK_ORDER = list(range(0,BLOCK_SIZE))
shuffle(BLOCK_ORDER)

def encrypt_block(block: str):
    to_ret = ""
    for index in BLOCK_ORDER:
        to_ret += block[index]
    return to_ret

print (f"Initial string '{PLAINTEXT}'")
sanitised_plaintext = ''.join([char for char in PLAINTEXT.lower() if char.isalpha()])

if len(sanitised_plaintext) % BLOCK_SIZE !=0:
    print(f"Sanitised string length {len(sanitised_plaintext)} so padding added")
    sanitised_plaintext += "a" * (BLOCK_SIZE - len(sanitised_plaintext) % BLOCK_SIZE)
print (f"Shuffling string '{sanitised_plaintext}'\nWith block size {BLOCK_SIZE} and block order {BLOCK_ORDER}")

block_arr = [sanitised_plaintext[i:i+BLOCK_SIZE] for i in range(0, len(sanitised_plaintext), BLOCK_SIZE)]

print (block_arr)
ciphertext = ''
for block in block_arr:
    enc_block = encrypt_block(block)
    print (f"{block} -> {enc_block}")
    ciphertext += enc_block

print(ciphertext)
