class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n 
        dp[-1] = 0 
        for i in range(n-2, -1, -1): 
            for j in range(i+1, n): 
                if abs(nums[i] - nums[j]) <= target and dp[j] != -1:
                    dp[i] = max(dp[i], 1 + dp[j])
        return dp[i]