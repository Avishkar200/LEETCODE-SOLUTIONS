class Solution:
    def countCommas(self, n: int) -> int:
        l=n-999
        t=0
        if l>0:
            t+=l
        return t