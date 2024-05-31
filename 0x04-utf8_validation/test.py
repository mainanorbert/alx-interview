def is_valid_utf8_encoding(integer):
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

# Test cases
"""x = 256
x = int(bin(x), 2)
print(x)"""
def func():
    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    data2 = [65]
    data3 = [80, 32, 111, 111, 108, 121, 116, 229, 65, 127, 256]
    for x in data3:
        if not is_valid_utf8_encoding(int(bin(x), 2)):
            return False
    return True

print(func())

