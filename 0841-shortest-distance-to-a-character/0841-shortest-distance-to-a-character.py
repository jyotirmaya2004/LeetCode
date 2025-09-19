class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [float('inf')] * n
        
        # Left to right
        prev = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            res[i] = i - prev
        
        # Right to left
        prev = float('inf')
        for i in range(n-1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev - i)
        
        return res

        