# Added using AI
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        st = set()
        
        for binary_str in nums:
            st.add(int(binary_str, 2))
        
        for i in range(1 << n):
            if i not in st:
                binary = bin(i)[2:]
                return binary.zfill(n)
        
        return ""