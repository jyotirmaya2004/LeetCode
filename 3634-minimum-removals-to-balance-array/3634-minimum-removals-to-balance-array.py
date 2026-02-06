class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, right, maxLen = 0, 0, 0

        while right < n:
            if nums[right] <= nums[left] * k:
                maxLen = max(maxLen, right - left + 1)
                right += 1
            else:
                left += 1

        return n - maxLen