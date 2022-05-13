#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Validates a set of characters represented by a list
    of integers.

    Must be UTF-8 Validated.
    Every integer is taken as a byte represented in
    8-bit binary number. The first byte in UTF-8
    is called the significant byte and states the
    number of bytes that the character will have.
    """
    byte_count = 0
    for byte in data:
        if byte_count == 0:
            if (byte >> 5) == 0b110:
                byte_count = 1
            elif (byte >> 4) == 0b1110:
                byte_count = 2
            elif (byte >> 3) == 0b11110:
                byte_count = 3
            elif (byte >> 2) == 0b111110:
                byte_count = 4
            elif (byte >> 1) == 0b1111110:
                byte_count = 5
            elif (byte >> 8):
                return False
        else:
            if (byte >> 6) == 0b10:
                byte_count -= 1
            else:
                return False
        return byte_count == 0
