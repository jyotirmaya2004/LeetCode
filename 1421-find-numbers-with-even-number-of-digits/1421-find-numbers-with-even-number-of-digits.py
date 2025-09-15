class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            # Check if number is in ranges with even digits
            if (10 <= num <= 99) or (1000 <= num <= 9999) or (100000 <= num <= 999999):
                count += 1
        return count