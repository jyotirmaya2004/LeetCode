class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        # Step 1: simulate gravity (right side)
        for i in range(m):
            empty = n - 1

            for j in range(n - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    empty = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j], boxGrid[i][empty] = boxGrid[i][empty], boxGrid[i][j]
                    empty -= 1

        # Step 2: rotate matrix
        res = [[None] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]

        return res