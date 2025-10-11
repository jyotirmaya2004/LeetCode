class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = Counter(power)
        arr = sorted(list(set(power)))
        n = len(arr)
        if n == 1:
            return arr[0] * counts[arr[0]]
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = arr[0] * counts[arr[0]]
        if arr[1] - arr[0] > 2:
            dp[2] = dp[1] + arr[1] * counts[arr[1]]
        else:
            dp[2] = max(dp[1], arr[1] * counts[arr[1]])
        for i in range(3, n + 1):
            if arr[i-1] - arr[i-2] > 2 and arr[i-1] - arr[i-3] > 2:
                dp[i] = dp[i-1] + arr[i-1] * counts[arr[i-1]]
            elif arr[i-1] - arr[i-3] > 2 and arr[i-1] - arr[i-2] < 3:
                dp[i] = max(dp[i-2] + arr[i-1] * counts[arr[i-1]], dp[i-1])
            elif arr[i-1] - arr[i-3] < 3 and arr[i-1] - arr[i-2] < 3:
                dp[i] = max(dp[i-3] + arr[i-1] * counts[arr[i-1]], dp[i-1])
        return dp[-1]
