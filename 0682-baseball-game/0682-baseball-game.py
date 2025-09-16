class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output=[]
        for i in range(len(operations)):
            if operations[i]=="+":
                output.append(output[-1]+output[-2])
            elif operations[i]=="D":
                output.append(output[-1]*2)
            elif operations[i]=="C":
                output.pop()
            else:
                output.append(int(operations[i]))
        return sum(output)
        