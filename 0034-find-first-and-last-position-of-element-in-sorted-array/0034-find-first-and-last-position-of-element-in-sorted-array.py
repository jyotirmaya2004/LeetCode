class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums) - 1
        first, last = -1, -1

        # find first occurrence
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                first = mid
                r = mid - 1   # keep going left
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l, r = 0, len(nums) - 1
        # find last occurrence
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                last = mid
                l = mid + 1   # keep going right
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [first, last]
