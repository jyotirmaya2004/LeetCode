class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        elif s==goal:
            return True
        else:
            g=list(goal)
            st=list(s)
            for i in range(len(s)):
                st=st[1:]+st[:1]
                if g==st:
                    return True
            return False

        