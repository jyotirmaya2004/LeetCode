class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1 = float('inf')
        min2 = float('inf')
        
        for x in nums[1:]:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x
                
        return nums[0] + min1 + min2