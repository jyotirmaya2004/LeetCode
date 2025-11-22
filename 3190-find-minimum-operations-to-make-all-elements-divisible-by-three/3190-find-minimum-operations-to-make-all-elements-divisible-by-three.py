class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for x in nums if x%3!=0)

        
        