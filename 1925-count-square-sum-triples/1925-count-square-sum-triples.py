class Solution(object):
    def countTriples(self, n):
        """
        Count Pythagorean triples where a² + b² = c² and a,b,c ≤ n
        
        :type n: int
        :rtype: int
        """
        sq = {i*i for i in range(1, n+1)}  # precompute all perfect squares
        r = 0                               # total triple count
        
        # 🔄 CHECK ALL PAIRS: For each possible (a,b) combination
        for i in range(1, n+1):
            temp = i*i                      # a²
            for j in range(i+1, n+1):
                s = temp + j*j              # a² + b²
                
                # ✅ VERIFY: Check if sum is a perfect square
                if s in sq:
                    r += 2                  # count both (a,b,c) and (b,a,c)
        
        return r