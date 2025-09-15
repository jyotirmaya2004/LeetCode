class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = set(wordlist)
        lower_map = {}
        vowel_map = {}

        def devowel(word: str) -> str:
            return "".join('*' if c.lower() in "aeiou" else c.lower() for c in word)

        # Preprocessing
        for w in wordlist:
            wl = w.lower()
            lower_map.setdefault(wl, w)
            vowel_map.setdefault(devowel(w), w)

        ans = []
        for q in queries:
            if q in words:
                ans.append(q)  # Rule 1
            elif q.lower() in lower_map:
                ans.append(lower_map[q.lower()])  # Rule 2
            elif devowel(q) in vowel_map:
                ans.append(vowel_map[devowel(q)])  # Rule 3
            else:
                ans.append("")  # No match
        return ans
