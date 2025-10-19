class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        trivanople = n  # store input as required

        s = str(trivanople)
        L = len(s)
        digits = [int(s[L - 1 - i]) for i in range(L)]  # LSB-first

        total = 0

        # lengths la and lb are the number of digits in a and b respectively (1..L)
        for la in range(1, L + 1):
            for lb in range(1, L + 1):
                dp = [1, 0]  # dp[c] = ways with carry = c
                for pos in range(L):
                    nd = digits[pos]
                    next_dp = [0, 0]

                    # allowed digits for a at this pos
                    a_start = 1 if pos < la else 0
                    a_end = 9 if pos < la else 0

                    # allowed digits for b at this pos
                    b_start = 1 if pos < lb else 0
                    b_end = 9 if pos < lb else 0

                    for carry in range(2):
                        ways = dp[carry]
                        if ways == 0:
                            continue
                        for a_dig in range(a_start, a_end + 1):
                            for b_dig in range(b_start, b_end + 1):
                                ssum = a_dig + b_dig + carry
                                if ssum % 10 == nd:
                                    nc = ssum // 10
                                    next_dp[nc] += ways

                    dp = next_dp

                # final carry must be zero for sum to equal n
                total += dp[0]

        return total