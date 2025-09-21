class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_s = float('-inf')

        for i in nums:
            s += i
            if max_s < s:
                max_s = s
            if s < 0:
                s = 0
        return max_s