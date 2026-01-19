class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rl, cl = len(mat), len(mat[0])
        ans = 0
        prefixsum = [[0] * (cl + 1) for _ in range(rl + 1)]

        for i in range(1, rl + 1):
            row_ps = 0
            for j in range(1, cl + 1):
                row_ps += mat[i - 1][j - 1]
                prefixsum[i][j] += prefixsum[i - 1][j] + row_ps

        def _sq_area(r, c, k):
            return (
                prefixsum[r + k][c + k]
                - prefixsum[r][c + k]
                - prefixsum[r + k][c]
                + prefixsum[r][c]
            )

        for k in range(1, min(rl, cl) + 1):
            found = False
            for r in range(rl - k + 1):
                for c in range(cl - k + 1):
                    if _sq_area(r, c, k) <= threshold:
                        found = True
                        break
                if found:
                    break
            if found:
                ans = k
            else:
                break

        return ans