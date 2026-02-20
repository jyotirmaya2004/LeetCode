class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        
        def fn(lo, hi): 
            if lo == hi: return ""
            vals = []
            ii, prefix = lo, 0
            for i in range(lo, hi):
                prefix += 1 if s[i] == "1" else -1 
                if prefix == 0: 
                    vals.append("1" + fn(ii+1, i) + "0")
                    ii = i+1
            return "".join(sorted(vals, reverse=True))
        
        return fn(0, len(s))