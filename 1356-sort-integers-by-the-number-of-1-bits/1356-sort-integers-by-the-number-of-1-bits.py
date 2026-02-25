class Solution:
    def find1(self, n: int) -> int:
        sum = 0
        while n > 0:
            sum += n % 2
            n //= 2
        return sum

    def sortByBits(self, arr):
        # Python does not have built-in multiset like C++
        # So we use list and sort each group (same idea)

        v = [[] for _ in range(15)]

        for i in range(len(arr)):
            v[self.find1(arr[i])].append(arr[i])

        ans = []

        for bucket in v:
            bucket.sort()   # keeps numbers ordered (like multiset)
            for num in bucket:
                ans.append(num)

        return ans