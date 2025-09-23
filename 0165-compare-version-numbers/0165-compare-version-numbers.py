class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split('.')
        s2 = version2.split('.')
        
        n = max(len(s1), len(s2))
        s1 += ["0"] * (n - len(s1))
        s2 += ["0"] * (n - len(s2))
        
        for i in range(n):
            if int(s1[i]) > int(s2[i]):
                return 1
            elif int(s1[i]) < int(s2[i]):
                return -1
        return 0
