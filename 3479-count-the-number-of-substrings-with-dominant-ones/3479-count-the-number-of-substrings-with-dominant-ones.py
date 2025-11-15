class Solution:
    def numberOfSubstrings(self, s: str) -> int:
            n = len(s)
            cumZeros = [0] * (n + 1) # DP-ish for count of zeros; cumZeros[i+1] = cumulative zeros up to i
            posZeros = [-1] # index positions of zeros in s
            posOnes = [-1] # index positions of ones in s

            res = 0

            for i, c in enumerate(s):
                if c == '1':
                    posOnes.append(i)
                    res += 1
                    curZeros = cumZeros[i] # cumulative zeros before i
                    curOnes = i - curZeros + 1 # number of ones we have is current index minus the zeros plus one
                    left = posZeros[curZeros - 1] # position before last zero
                else:
                    posZeros.append(i)
                    curZeros = cumZeros[i] + 1 # cumulative zeros before i, +1 for the current zero 
                    curOnes = i - curZeros + 1 # number of ones we have is current index minus the zeros plus one
                    left = posOnes[curOnes] # position before the last one

                cumZeros[i + 1] = curZeros # set the next cumulative zeros count, cumZeros[i+1] represents s[:i]

                right = i
                while left >= 0:
                    countZero = curZeros - cumZeros[left] # Zeros in range [left, i]
                    countOne = i - left + 1 - countZero # Ones in range [left, i]

                    sqZero = countZero * countZero
                    if sqZero <= countOne:
                        if s[left] == "1": # if jump ended on a 1, only count current full substring [left, right]
                            res += 1
                        else:
                            res += right - left # if jump ended on a 0, count all substrings in [left, right]

                        right = left

                        nextZero = curZeros - ceil(sqrt(countOne + 1)) + 1 # index in posZeros to jump to next that's valid (enough ones to satisfy the condition)
                        left = posZeros[nextZero] if nextZero >= 0 else -1

                    else:
                        if s[left] == "0":
                            res += right - left - 1 # if jump ended on a 0, count all substrings in [left, right], excluding the full substring due to the jump logic

                        right = left
                        nextOne = curOnes - sqZero + 1 # at least sqZero ones to satisfy condition
                        left = posOnes[nextOne] if nextOne >= 0 else -1

                if curZeros * curZeros <= curOnes: # if entire range is dominant, count all remaining valid substrings up to right from s[0]
                    res += right
            return res