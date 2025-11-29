class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0
        for num in nums:
            total += num
        return total % k
        #return min(total % k, k - total % k)
        