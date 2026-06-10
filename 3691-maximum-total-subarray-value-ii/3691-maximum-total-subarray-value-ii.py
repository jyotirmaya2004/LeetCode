import heapq
from math import log2
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        heap = []

        # sending all last elements of sequences those are are max valies for fixed l to n-1

        

        #spare tree implememntation 

        K = int(log2(n)) + 1
        stMax  =  [[0] * K for _ in range(n)]     
        stMin  =  [[0] * K for _ in range(n)]

        for i in range(n) :
            stMax[i][0] = nums[i]
            stMin[i][0] = nums[i]

        j = 1
        while (1 << j) <= n :
            i = 0
            while i + (1<<j) <= n :
                stMax[i][j] = max(stMax[i][j-1] , stMax[i + (1 << (j-1))][j-1])
                stMin[i][j] = min(stMin[i][j-1] , stMin[i + (1 << (j-1))][j-1])

                i += 1
            j += 1
        def queryMax(l,r) :
            k = int(log2(r - l + 1))

            return max(stMax[l][k] , stMax[r - (1 << k) + 1][k])
        def queryMin(l,r) :
            k = int(log2(r - l + 1))

            return min(stMin[l][k] , stMin[r - (1 << k) + 1][k])

        def getValue(l ,r) :
            return queryMax(l,r) - queryMin(l,r)

        

        for l in range(n) :
            value = getValue(l , n-1)
            heapq.heappush(heap , (-value , l , n-1))

        # print(heap)

            




        ans = 0

        for _ in range(k) :
            value , l , r = heapq.heappop(heap)
            value = -value
            ans += value

            if r > l :
                newVal = getValue(l , r-1)
                heapq.heappush(heap , (-newVal , l , r-1))
        return ans


        