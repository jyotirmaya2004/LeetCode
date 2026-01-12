class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0

        i = 0
        while(i < len(points) - 1):

            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[i + 1][0]
            y2 = points[i + 1][1]
            
            d1 = x2 - x1
            d2 = y2 - y1

            d1_abs = abs(d1)
            d2_abs = abs(d2)
            
            if(d1_abs <= d2_abs):

                time += d1_abs

                if(d2 >= 0):
                    time += abs(y2 - y1 - d1_abs)

                else:
                    time += abs(y2 - y1 + d1_abs)
                
            else:
                
                time += d2_abs

                if(d1 >= 0):
                    time += abs(x2 - x1 - d2_abs)
                
                else:
                    time += abs(x2 - x1 + d2_abs)

            i += 1

        return time