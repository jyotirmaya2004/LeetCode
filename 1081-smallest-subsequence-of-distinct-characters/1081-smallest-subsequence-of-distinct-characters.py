class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Store the last occurrence of every character
        lastPos = {}
        for i, char in enumerate(s):
            lastPos[char] = i

        stack = []
        included = set()

        for i, char in enumerate(s):
            # Skip duplicate characters
            if char in included:
                continue

            # Remove larger characters if they appear again later
            while (
                stack
                and char < stack[-1]
                and lastPos[stack[-1]] > i
            ):
                included.remove(stack.pop())

            stack.append(char)
            included.add(char)

        return "".join(stack)
        for i, char in enumerate(s):
            # Skip duplicate characters
            if char in included:
                continue

            # Remove larger characters if they appear again later
            while (
                stack
                and char < stack[-1]
                and lastPos[stack[-1]] > i
            ):
                included.remove(stack.pop())

            stack.append(char)
            included.add(char)

        return "".join(stack)