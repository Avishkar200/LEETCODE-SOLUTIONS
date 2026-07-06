class Solution:
    def isHappy(self, n: int) -> bool:
        d=set()
        if n==7 or n==1:
            return True
        while n!=1 and n not in d:
            d.add(n)
            g=0
            s=str(n)
            for i in s:
                g+=int(i)**2 
            if g==1:
                return True
            else:
                n=g

        return False


        
        