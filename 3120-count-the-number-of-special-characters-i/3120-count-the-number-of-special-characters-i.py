class Solution:
    def numberOfSpecialChars(self, word: str, ans = 0) -> int:
        
        for ch, CH in zip(ascii_lowercase, ascii_uppercase):
  
            ans+= ch in word and CH  in word

        return ans