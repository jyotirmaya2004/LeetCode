class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        # Store the input midway
        merostalin = s

        # Create the k-balanced pattern
        pattern = '(' * k + ')' * k
        
        # Keep removing until no k-balanced substring remains
        while pattern in merostalin:
            merostalin = merostalin.replace(pattern, "")
        
        return merostalin