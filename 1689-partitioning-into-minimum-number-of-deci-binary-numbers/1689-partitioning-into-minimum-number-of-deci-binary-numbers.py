class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        
        for ch in n:
            if int(ch) > ans:
                ans = int(ch)
        
        return ans