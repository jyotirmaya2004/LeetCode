class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr=[]
        if n==0:
            return arr
        elif n==1:
            arr.append(0)
            return arr
        elif n%2==0:
            for i in range(1,(n//2)+1):
                arr.append(+i)
                arr.append(-i)
        else:
            arr.append(0)
            for i in range(1,(n//2)+1):
                arr.append(+i)
                arr.append(-i)
        return arr