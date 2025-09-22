class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums.sort()
        output=[]
        c=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                c+=1
                continue
            else:
                output.append(c)
                c=1
        output.append(c)
        max_f=max(output)
        return output.count(max_f)*max_f


        