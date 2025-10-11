from typing import List
import bisect

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Step 1: Group same power values
        power.sort()
        groups = []
        curr = power[0]
        total = curr
        for i in range(1, len(power)):
            if power[i] != curr:
                groups.append((curr, total))
                curr = power[i]
                total = curr
            else:
                total += curr
        groups.append((curr, total))

        # Step 2: Maintain sorted dp states by value
        # dp_values[i] = value, dp_sums[i] = max sum achievable up to this value
        dp_values = [groups[0][0]]
        dp_sums = [groups[0][1]]

        for i in range(1, len(groups)):
            val, damage = groups[i]

            # Find index of last value ≤ val - 3 (non-conflicting)
            idx = bisect.bisect_right(dp_values, val - 3) - 1

            if idx >= 0:
                include = dp_sums[idx] + damage
            else:
                include = damage

            # Exclude option → previous max
            exclude = dp_sums[-1]

            best = max(include, exclude)

            dp_values.append(val)
            dp_sums.append(best)

        return dp_sums[-1]