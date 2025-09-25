"""
Toggle Bits after MSB

Description: Given a positive integer, convert to binary, then toggle all bits from the most significant bit (inclusive) to the least significant bit, and return the integer value.

Input: single integer N

Output: integer after toggling bits
"""
n=13   #binary value = 1101 
a=n.bit_length()    #bit length = 4
mask=(1<<a) -1      #mask = (1 << 4) - 1 = 16 - 1 = 15 → binary 1111.
print(n^mask)       #13 ^ 15 = 1101 ^ 1111 = 0010 (binary) = 2.
