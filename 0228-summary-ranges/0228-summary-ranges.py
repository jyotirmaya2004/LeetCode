class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: 
            return []
        start=0
        end=0
        output=[]
        for i in range(len(nums)):
            if i==0:
                start=nums[i]
                continue
            elif nums[i-1]+1==nums[i]:
                continue
            else:
                end=nums[i-1]
            if start==end:
                output.append(f"{start}")
            else:
                output.append(f"{start}->{end}")
            start=nums[i]
        end=nums[-1]
        if start==end:
            output.append(f"{start}")
        else:
            output.append(f"{start}->{end}")
        return output

            
        