class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        Find maximum sum of subarray with length divisible by k
        
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        p = [0] * (n + 1)  # prefix sum array
        dp = [float('-inf')] * n  # dp[i] = max sum ending at i with length divisible by k
        result = float('-inf')
        
        for i in range(n):
            # Build prefix sum
            p[i + 1] = p[i] + nums[i]
            
            # Process positions where we can form valid subarrays
            if i >= k - 1:
                # Sum of last k elements
                temp_sum = p[i + 1] - p[i + 1 - k]
                
                # Option 1: Start new subarray of length k
                dp[i] = temp_sum
                
                # Option 2: Extend previous valid subarray
                if i >= k and dp[i - k] != float('-inf'):
                    dp[i] = max(dp[i], dp[i - k] + temp_sum)
                
                # Track maximum result
                result = max(result, dp[i])
        
        return result
        