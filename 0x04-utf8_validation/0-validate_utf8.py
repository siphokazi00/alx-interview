#!/usr/bin/python3
"""
Determines if a given set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    num_bytes = 0

    for byte in data:
        # Check the byte pattern
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                num_bytes = 0  # 1-byte character
            elif (byte >> 5) == 0b110:
                num_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                num_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                num_bytes = 3  # 4-byte character
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
