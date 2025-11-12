class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        num1, overall_g = 0, 0

        for x in nums:
            if x == 1:
                num1 += 1
            overall_g = gcd(overall_g, x)

        if num1 > 0:
            return n - num1
        if overall_g > 1:
            return -1

        min_len = n
        for i in range(n):
            g = nums[i]
            if g == 1:
                min_len = 1
                break  
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break  
        return min_len + n - 2