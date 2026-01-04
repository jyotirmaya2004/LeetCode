class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        sum_val = 0
        carry = 0
        
        # Traverse from the last digit to the first
        for i in range(n - 1, -1, -1):
            # Add 1 only if it is the last digit, otherwise just add the carry
            adder = 1 if i == n - 1 else 0
            sum_val = digits[i] + adder + carry
            
            # If no carry is generated, update and return
            if sum_val <= 9:
                digits[i] = sum_val
                return digits
            
            # If carry is generated
            digits[i] = sum_val % 10
            carry = sum_val // 10
            
        # If the loop completes and carry is still non-zero
        if carry != 0:
            digits.insert(0, carry)
            
        return digits