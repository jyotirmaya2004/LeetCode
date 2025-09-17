class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st=s.rstrip()
        output=""
        for i in range(-1,-(len(st)+1),-1):
            if st[i]==" ":
                return len(output)
            else:
                output+=st[i]
        return len(output)


        