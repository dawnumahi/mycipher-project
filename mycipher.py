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
