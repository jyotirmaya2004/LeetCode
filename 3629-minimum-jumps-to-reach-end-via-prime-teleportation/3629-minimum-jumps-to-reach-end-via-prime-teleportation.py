# Pre-calculating prime factors for all numbers up to 1,000,000
# This runs once and stays in memory for all test cases
MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]: # If i is prime
        for j in range(i, MX, i):
            factors[j].append(i)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        # Create a map to find where primes are located
        edges = defaultdict(list)
        for i, a in enumerate(nums):
            # If the number is prime (has only 1 prime factor)
            if len(factors[a]) == 1:
                edges[a].append(i)
        
        res = 0
        seen = [False] * n
        seen[-1] = True # Start from the end
        q = [n - 1]
        
        while q:
            q2 = [] # To store the next level of jumps
            for i in q:
                if i == 0: # Reached the start!
                    return res
                
                # Check neighbor to the left
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                
                # Check neighbor to the right
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                
                # Check all teleport options for current number's prime factors
                for p in factors[nums[i]]:
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    # Clear the prime teleport station so we don't reuse it
                    edges[p].clear()
            
            q = q2
            res += 1