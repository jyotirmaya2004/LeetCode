class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Extract and sort squares by bottom y-coordinate
        sq = sorted([y, l] for x, y, l in squares)

        def areaUnder(y):
            area = 0
            for s in sq: 
                if s[0] + s[1] <= y:  # Square is fully below the line
                    area += (s[1] ** 2)
                elif s[0] < y < (s[0] + s[1]):  # Square is partially cut by the line
                    h = y - s[0]  # Height below the line
                    area += (s[1] * h)  # Area of the rectangle below the line
                else:  # Square is fully above the line
                    break
            return area

        # Calculate total area and find half
        half = sum(l**2 for _, l in sq) / 2
        
        # Binary search to find the y-coordinate where area below equals half
        l = 0
        r = max(y + l for y, l in sq)  # Upper bound is the top of the highest square
        
        while r - l > 1e-6:  # Continue until desired precision
            mid = (l + r) / 2
            area_under = areaUnder(mid)
            
            if area_under < half:
                l = mid
            else:
                r = mid
        
        return l