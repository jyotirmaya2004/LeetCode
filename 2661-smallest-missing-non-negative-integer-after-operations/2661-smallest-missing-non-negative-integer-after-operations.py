class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counts = [0] * value

        for num in nums:
            counts[num % value] += 1
        
        min_i = 0
        for i in range(1, value):
            if counts[i] < counts[min_i]:
                min_i = i
        
        return value * counts[min_i] + min_i