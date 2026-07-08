class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=operations
        s=[]
        for i in range(len(a)):
            if a[i] not in ["C","+","D"]:
                s.append(int(a[i]))
            else:
                if a[i]=="C":
                    s.pop()
                if a[i]=="+":
                    s.append(s[-1]+s[-2])
                if a[i]=="D":
                    s.append(2*s[-1])
        
        return sum(s)
            



        