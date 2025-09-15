class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(str(x) for x in digits)
        num=int(s)
        num+=1
        s2=str(num)
        return [int(x) for x in (s2)]
        