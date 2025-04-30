#!/usr/bin/env python3
import sys
import string

def caesar(s, shift):
    out = []
    for char in s.upper():
        if char in string.ascii_uppercase:
            temp = (ord(char) - ord('A') + shift) % 26
            out.append(chr(ord('A') + temp))
    return ''.join(out)

def format_blocks(text, block_size = 5, blocks_per_line=10):
    blocks = [ text[i:i+block_size]
            for i in range(0, len(text), block_size)]
    for i in range(0, len(blocks), blocks_per_line):
        print(' '.join(blocks[i:i+blocks_per_line]))


