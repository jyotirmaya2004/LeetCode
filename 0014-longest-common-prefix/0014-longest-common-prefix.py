class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        newstr=""
        first_word=min(strs, key=len)
        j=0
        for i in first_word:
            for k in strs:
                if i!=k[j]:
                    return newstr
            newstr+=i
            j+=1
        return newstr

        