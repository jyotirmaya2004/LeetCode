class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(x%10+x//10%10+x//100%10+x//1000%10+x//10000%10 for x in nums)
        