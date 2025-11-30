class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total < p:
            return -1
        if total % p == 0:
            return 0
        extra = total % p
        # remainder, rightMostPosition
        memo = {}
        memo[0] = -1
        cur = 0
        ans = n
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            r = (cur - extra) % p
            if r in memo:
                ans = min(ans, i - memo[r])
            memo[cur] = i
        return ans if ans < n else -1