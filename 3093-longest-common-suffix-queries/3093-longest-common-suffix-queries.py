class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = {}
        for i,word in enumerate(wordsContainer):
            spot = trie
            if None not in spot or spot[None][1] > len(word):
                spot[None] = (i,len(word))
            for c in reversed(word):
                if c not in spot:
                    spot[c] = {}
                spot = spot[c]
                if None not in spot or spot[None][1] > len(word):
                    spot[None] = (i,len(word))
        ans = []
        for word in wordsQuery:
            spot = trie
            for c in reversed(word):
                if c not in spot:
                    break
                spot = spot[c]
            ans.append(spot[None][0])
        return ans