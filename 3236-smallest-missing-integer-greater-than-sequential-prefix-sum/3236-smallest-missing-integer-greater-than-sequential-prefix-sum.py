class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum=nums[0]
        j=0
        for i in range(1,len(nums)):
            if nums[j]+1==nums[i]:
                sum+=nums[i]
            else:
                break
            j+=1
        while(1):
            if sum in nums:
                sum+=1
            else:
                return sum


        