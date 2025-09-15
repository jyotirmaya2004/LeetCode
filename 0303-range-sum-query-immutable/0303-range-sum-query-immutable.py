class NumArray:

    def __init__(self, nums: List[int]):
        # store the array
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        # compute sum directly
        return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)