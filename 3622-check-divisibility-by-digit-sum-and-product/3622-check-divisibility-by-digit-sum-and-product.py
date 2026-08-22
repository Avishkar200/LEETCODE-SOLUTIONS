class Solution:
    def checkDivisibility(self, n: int) -> bool:
        l=str(n)
        s=0
        m=1
        for i in range(len(l)):
            s+=int(l[i])
            m*=int(l[i])
        if n%(s+m)==0:
            return True
        else:
            return False

        