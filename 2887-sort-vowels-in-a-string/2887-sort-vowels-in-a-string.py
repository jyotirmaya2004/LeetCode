class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_list=[]
        s_list=list(s)
        for i in s:
            if i=='a' or i=='i' or i=='e' or i=='o' or i=='u' or i=='A' or i=='I' or i=='E' or i=='O' or i=='U':
                vowel_list.append(i)
        vowel_list.sort()
        j=0
        for k in range(len(s)):
            i=s[k]
            if i=='a' or i=='i' or i=='e' or i=='o' or i=='u' or i=='A' or i=='I' or i=='E' or i=='O' or i=='U':
                s_list[k]=vowel_list[j]
                j+=1
        return "".join(s_list)