class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnt, ans, used = 0, [], [0] * (len(A)+1)
        for a, b in zip(A, B):
            cnt += used[a]
            used[a] = 1
            cnt += used[b]
            used[b] = 1
            ans.append(cnt)
        return ans