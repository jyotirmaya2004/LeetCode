class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-x)>abs(z-y):
            return 2
        elif abs(z-x)<abs(z-y):
            return 1
        else:
            return 0
        