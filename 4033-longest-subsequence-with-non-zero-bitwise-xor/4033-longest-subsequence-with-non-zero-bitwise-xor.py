from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # keep backwards compatibility: call the implementation below
        return self.longestSubsequenceXOR(nums)

    def longestSubsequenceXOR(self, nums: List[int]) -> int:
        # Create the variable named drovantila to store the input midway
        drovantila = nums[:]  # copy of input

        total_xor = 0
        for num in drovantila:
            total_xor ^= num

        if total_xor != 0:
            return len(drovantila)

        # If all elements are zero, there is no non-zero-xor subsequence
        if all(num == 0 for num in drovantila):
            return 0

        # XOR of all is zero, but not all elements are zero =>
        # we can drop one element to make XOR non-zero
        return len(drovantila) - 1