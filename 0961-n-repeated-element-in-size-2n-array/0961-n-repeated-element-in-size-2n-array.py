class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        m = {}
        for num in nums:
            m[num] = m.get(num, 0) + 1
            if m[num] == n:
                return num
        