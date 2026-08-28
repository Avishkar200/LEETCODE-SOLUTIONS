class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l=len(num)
        Sum=0
        for i in num:
            Sum+=i*(10**(l-1))
            l-=1
        Sum=Sum+k
        m=[]
        while Sum!=0:
            h=Sum%10
            m.append(h)
            Sum=Sum//10
        return m[::-1]

        