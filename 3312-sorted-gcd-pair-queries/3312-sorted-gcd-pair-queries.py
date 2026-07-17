MX = 50001
divisors = [[] for _ in range(MX)]
for x in range(1, MX):
    for y in range(x, MX, x):
        divisors[y].append(x)


class Solution:
    def gcdValues(self, A: List[int], queries: List[int]) -> List[int]:
        M = max(A)
        countA = Counter(A)
        countD = Counter()  # countD[d]: number of (i) with A[i] % d == 0
        for x, freq in countA.items():
            for d in divisors[x]:
                countD[d] += freq

        countG = Counter()  # countG[g]: number of (i < j) with gcd(A[i], A[j]) == g
        for g in range(M, 0, -1):
            c = countD[g]
            if c <= 1:
                continue
            countG[g] = c * (c - 1) // 2
            countG[g] -= sum(countG[x] for x in range(2 * g, M + 1, g))

        glist = [g for g, v in reversed(countG.items())]
        vlist = [v for g, v in reversed(countG.items())]
        Pvlist = list(accumulate(vlist))

        ans = []
        for q in queries:
            i = bisect_left(Pvlist, q + 1)
            ans.append(glist[i])
        return ans