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

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 mycipher.py <shift>")
    shift = int(sys.argv[1]) % 26

    plaintext = sys.stdin.read()
    cipher = caesar(plaintext, shift)
    format_blocks(cipher)

if __name__ = "__main__":
    main()
