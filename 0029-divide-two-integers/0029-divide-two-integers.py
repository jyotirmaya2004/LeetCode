class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:
            temp, multiple = b, 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            res += multiple
        if (dividend < 0) ^ (divisor < 0):
            res = -res

        return max(-(2**31), min(res, 2**31 - 1))
