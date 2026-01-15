class Solution:
 def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
     vBars.sort()
     hBars.sort()

     hmax = vmax = hcur = vcur = 1

     for i in range(len(hBars)):
         if hBars[i] == hBars[i - 1] + 1:
             hcur += 1
         else:
             hcur = 1
         hmax = max(hmax, hcur)

     for i in range(len(vBars)):
         if vBars[i] == vBars[i - 1] + 1:
             vcur += 1
         else:
             vcur = 1
         vmax = max(vmax, vcur)

     side = min(hmax, vmax) + 1
     return side * side