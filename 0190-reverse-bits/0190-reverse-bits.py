class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        
        for _ in range(32):
            result <<= 1          # make space for next bit
            result |= (n & 1)     # take last bit of n
            n >>= 1               # shift n right
        
        return result