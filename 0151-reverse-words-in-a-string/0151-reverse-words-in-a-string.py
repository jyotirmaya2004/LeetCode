class Solution:
    def reverseWords(self, s: str) -> str:
        st=s.split()
        st.reverse()
        return " ".join(st)
        