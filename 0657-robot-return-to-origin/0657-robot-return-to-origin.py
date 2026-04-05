class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        position  = 0
        d = {'R': 1, "L": -1, 'U': 1j, 'D': - 1j}

        for ch in moves:
            position+= d[ch]

        return position == 0