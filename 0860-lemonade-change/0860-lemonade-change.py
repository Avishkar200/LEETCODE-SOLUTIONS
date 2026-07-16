class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5=0
        bill10=0
        bill20=0
        for i in bills:
            if i==5:
                bill5+=1
            elif i==10:
                bill10+=1
                bill5-=1
                if bill5<0:
                    return False
            elif i==20:
                bill20+=1
                bill5-=1
                if bill10>0:
                    bill10-=1
                else:
                    bill5-=2
                if bill5<0 or bill10<0:
                    return False
        return True
        