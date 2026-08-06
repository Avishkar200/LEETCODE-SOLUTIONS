class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            s=str(n)
            j=1
            for i in s:
                j*=int(i)
            if j%t==0:
                return n
                break
            else:
                n+=1
            