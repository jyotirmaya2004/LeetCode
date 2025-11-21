class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        charMap = {}
        for i, c in enumerate(s):
            if c not in charMap:
                charMap[c] = []
            charMap[c].append(i)

        palCount = 0

        for c, positions in charMap.items():
            if len(positions) < 2:
                continue  # need at least two occurrences for aba

            first = positions[0]
            last = positions[-1]

            if last - first < 2:
                continue  # no space for middle character

            # All distinct middle characters between first and last
            middle_chars = set(s[first + 1 : last])
            palCount += len(middle_chars)

        return palCount