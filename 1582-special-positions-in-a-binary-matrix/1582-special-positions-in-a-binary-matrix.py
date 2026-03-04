class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowSpecial = defaultdict(int)
        for _, row in enumerate(mat):
            if row.count(1) == 1:
                rowSpecial[row.index(1)] = 1

        specialCount = 0
        for i in range(len(mat[0])):
            if (col := [row[i] for row in mat]).count(1) == 1:
                specialCount += rowSpecial[i]

        return specialCount
