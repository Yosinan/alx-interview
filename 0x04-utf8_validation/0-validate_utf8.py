#!/usr/bin/python3
"""
    UTF-8 Validation
"""


def validUTF8(data):
    """
        Method that determines if a given data set represents a valid UTF-8
        encoding.
        Args:
            data: The data to validate.
        Return:
            True if data is a valid UTF-8 encoding, else return False.
    """
    no_bytes = 0

    for num in data:
        byte = num & 0xff
        if no_bytes == 0:
            bit_mask = 1 << 7
            while bit_mask & byte:
                no_bytes += 1
                bit_mask >>= 1
            if no_bytes == 0:
                continue
            if no_bytes == 1 or no_bytes > 4:
                return False
        else:
            bit_mask1 = 1 << 7
            bit_mask2 = 1 << 6
            if not (byte & bit_mask1 and not (byte & bit_mask2)):
                return False
        no_bytes -= 1
    return no_bytes == 0
