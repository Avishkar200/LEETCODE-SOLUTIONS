class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        a=""
        l=[]
        for i in s:
            if i!="0":
                a+=i
                l.append(int(i))
        if len(a)==0:
            return 0
        else:
            return int(a)*sum((l))


        