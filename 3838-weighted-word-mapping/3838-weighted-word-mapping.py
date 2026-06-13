class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=[]
        for w in words:
            Sum=sum( weights[ord(c)-97] for c in w)
            ans.append(chr(97+25-Sum%26))
        return "".join(ans)
        