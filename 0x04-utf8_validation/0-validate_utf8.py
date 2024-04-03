#!/usr/bin/python3
"""module that determines if a given
data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """function determines if a given data set
    represents a valid UTF-8 encoding"""
    for x in data:
        if not is_valid_utf8_encoding(int(bin(x), 2)):
            return False
    return True


def is_valid_utf8_encoding(integer):
    """function that determines of int is utf8"""
    if integer < 0x80:
        # Single-byte character
        return True
    elif integer < 0x800:
        # Two-byte character
        return (integer & 0xE0) == 0xC0
    elif integer < 0x10000:
        # Three-byte character
        return (integer & 0xF0) == 0xE0
    elif integer < 0x110000:
        # Four-byte character
        return (integer & 0xF8) == 0xF0
    else:
        return False
