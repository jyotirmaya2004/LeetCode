class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle=[]
        for i in range(rowIndex+1):
            arr1=[1]*(i+1)
            for j in range(1,i):
                arr1[j]=triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append(arr1)
        return triangle[rowIndex]
        