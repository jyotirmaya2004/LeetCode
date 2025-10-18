class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        smallest_elem = nums[0] - k - 1

        for num in nums:
            if num + k > smallest_elem:
                res += 1
                smallest_elem = max(smallest_elem + 1, num - k)
        
        return res